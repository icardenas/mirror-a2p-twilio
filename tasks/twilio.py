import django
django.setup()

from mrq.task import Task
from mrq.job import queue_job
from twilio_management.controller.phone_number_controller import PhoneNumberController
from twilio_management.models import PhoneNumber

class GetInformation(Task):
    def run(self, params):
        background_job_id = queue_job(
            "tasks.twilio.FillPhoneNumbers", params, queue="medium", delay=0
        )
        return {"background_job_id": background_job_id}

class FillPhoneNumbers(Task):
    def run(self, params):
        phone_number = PhoneNumberController(PhoneNumber)
        phone_number.sync_information()
        # background_job_id = queue_job(
        #     "tasks.twilio.FillMessagingService", params, queue="medium", delay=0
        # )
        # return {"background_job_id": background_job_id}
        return phone_number.get_stast()

class FillMessagingService(Task):
    def run(self, params):
        #call helper function
        return {"Finish": True}
