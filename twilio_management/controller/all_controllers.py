from twilio_management.controller.abstract_controller import AbstractController
from typing import Iterator, List

from twilio_management.models import Compliance, PhoneNumber

import logging

logger = logging.getLogger(__name__)
class PhoneNumberController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.incoming_phone_numbers.stream()

    def post_save(self, instance) -> None:
        pass


class MessagingServicesController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.messaging.services.stream()

    def post_save(self, instance) -> None:
        self._get_phone_numbers(instance)
        self._get_compliance(instance)

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
        return new_compliances
        
    
    def _get_phone_numbers(self, instance) -> List[PhoneNumber]:
        new_phone_numbers = []
        phone_numbers = self.twilio_client.connection.messaging \
                      .services(instance.sid) \
                      .phone_numbers \
                      .list(limit=20)
        for twilio_phone_number in phone_numbers:
            db_phone_number = PhoneNumber.objects.filter(phone_number=twilio_phone_number.phone_number).first()
            logger.error(db_phone_number)
            logger.error(twilio_phone_number.phone_number)
            db_phone_number.messaging_service = instance
            db_phone_number.save()
            new_phone_numbers.append(db_phone_number)
        
        return new_phone_numbers
        
