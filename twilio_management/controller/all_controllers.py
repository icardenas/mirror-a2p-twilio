from twilio_management.controller.abstract_controller import AbstractController
from typing import Iterator, List

from twilio_management.models import A2PBrand, AbstractModel, BrandRegistration, Compliance, PhoneNumber

import logging

logger = logging.getLogger(__name__)
class PhoneNumberController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.incoming_phone_numbers.stream()

    def post_save(self, instance) -> None:
        if instance.sms_method != 'GET' or \
            instance.sms_fallback_method != 'GET' or  \
            'application_message_sms' not in instance.sms_url or \
            'application_message_sms' not in instance.sms_url:
            #Only for Apploi
            APPLOI_URL = "https://api.apploi.com/v1/application_message_sms/get-received"
            # incoming_phone_number = self.twilio_client.connection.incoming_phone_numbers(
            #     instance.sid
            # ).update(sms_method='GET', sms_fallback_method='GET', 
            #     sms_url=APPLOI_URL, 
            #     sms_fallback_url=APPLOI_URL)
            print('updated this', instance.sid, instance.sms_method, instance.sms_fallback_method, instance.sms_url, instance.sms_fallback_url)


class MessagingServicesController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.messaging.services.stream()

    def post_save(self, instance) -> None:
        self._get_phone_numbers(instance)
        self._get_compliance(instance)

    def _get_brandregistration(self, compliance) -> BrandRegistration:
        db_brandregistration = None
        try:
            twilio_brandregistration = self.twilio_client.connection.messaging.brand_registrations(compliance.brand_registration_sid).fetch()
            print(twilio_brandregistration.sid)
            db_brandregistration = self.save_information(twilio_brandregistration, BrandRegistration)
            db_brandregistration.save()
            self._get_a2p_brand(db_brandregistration)
        except Exception as e:
            logger.error(e)
        return db_brandregistration
    
    def _get_a2p_brand(self, db_brandregistration) -> A2PBrand:
        db_a2p_brand = None
        try:
            a2p_brand = self.twilio_client.connection.trusthub \
                        .trust_products(db_brandregistration.a2p_profile_bundle_sid).fetch()
            db_a2p_brand = self.save_information(a2p_brand, A2PBrand)
            db_brandregistration.a2p_brand = db_a2p_brand
            db_brandregistration.save()
        except Exception as e:
            logger.error(f"Message {str(e)}")
        return db_a2p_brand

    def _get_compliance(self, instance) -> List[Compliance]:
        new_compliances = []
        compliances = self.twilio_client.connection.messaging.services(instance.sid) \
                .us_app_to_person \
                .list(limit=20)
        for twilio_compliance in compliances:
            db_compliance = self.save_information(twilio_compliance, Compliance)
            db_compliance.messaging_service = instance
            db_compliance.save()
            new_compliances.append(db_compliance)
            self._get_brandregistration(db_compliance)
        return new_compliances
        
    
    def _get_phone_numbers(self, instance) -> List[PhoneNumber]:
        new_phone_numbers = []
        phone_numbers = self.twilio_client.connection.messaging \
                      .services(instance.sid) \
                      .phone_numbers \
                      .list(limit=20)
        for twilio_phone_number in phone_numbers:
            db_phone_number = PhoneNumber.objects.filter(phone_number=twilio_phone_number.phone_number).first()
            # logger.error(db_phone_number, twilio_phone_number.phone_number)
            db_phone_number.messaging_service = instance
            db_phone_number.save()
            new_phone_numbers.append(db_phone_number)
        
        return new_phone_numbers
        
class BrandRegistrationController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.messaging.brand_registrations.stream()

    def post_save(self, instance) -> None:
        db_a2p_brand = None
        try:
            a2p_brand = self.twilio_client.connection.trusthub \
                        .trust_products(instance.a2p_profile_bundle_sid).fetch()
            db_a2p_brand = self.save_information(a2p_brand, A2PBrand)
            instance.a2p_brand = db_a2p_brand
        except Exception as e:
            logger.error(f"Message {str(e)}")
        return db_a2p_brand

class CustomerProfileController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.trusthub.customer_profiles.stream(limit=5000, page_size=1000)

    def post_save(self, instance) -> None:
        pass