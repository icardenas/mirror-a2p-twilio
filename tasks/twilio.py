import django

django.setup()

from mrq.task import Task
from mrq.job import queue_job
from twilio_management.controller.all_controllers import (
    BrandRegistrationController,
    CustomerProfileController,
    PhoneNumberController,
    MessagingServicesController,
)
from twilio_management.models import A2PBrand, BrandRegistration, CustomerProfile, MessagingService, PhoneNumber


class GetInformation(Task):
    def run(self, params):
        PhoneNumber.truncate()
        MessagingService.truncate()
        BrandRegistration.truncate()
        A2PBrand.truncate()
        background_job_id = queue_job(
            "tasks.twilio.FillPhoneNumbers", params, queue="medium"
        )
        return {"background_job_id": background_job_id}


class FillPhoneNumbers(Task):
    def run(self, params):
        phone_number = PhoneNumberController(PhoneNumber)
        phone_number.sync_information()
        background_job_id = queue_job(
            "tasks.twilio.FillMessagingService", params, queue="medium"
        )
        return {**phone_number.get_stast(), **{"background_job_id": background_job_id}}


class FillMessagingService(Task):
    def run(self, params):
        messaging_service = MessagingServicesController(MessagingService)
        messaging_service.sync_information()
        background_job_id = queue_job(
            "tasks.twilio.FillCustomerProfile", params, queue="medium"
        )
        return {**messaging_service.get_stast(),**{"background_job_id": background_job_id}}
class FillCustomerProfile(Task):
    def run(self, params):
        CustomerProfile.truncate()
        customer_profile = CustomerProfileController(CustomerProfile)
        customer_profile.sync_information()
        background_job_id = queue_job(
            "tasks.twilio.FillBrandRegistration", params, queue="medium"
        )
        return customer_profile.get_stast()

class FillBrandRegistration(Task):
    def run(self, params):
        brand_registration = BrandRegistrationController(BrandRegistration)
        brand_registration.sync_information()
        return brand_registration.get_stast()
