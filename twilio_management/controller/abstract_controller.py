import abc
from typing import Any
from twilio_management.utils.client import TwilioClient
import logging
from django.db import transaction

logger = logging.getLogger(__name__)


class AbstractController(abc.ABC):
    def __init__(self, model: Any) -> None:
        self.twilio_client = TwilioClient()
        self.stast: dict = {"amount_sucessful": 0, "amount_error": 0}
        self.model = model
        self.truncat_model()

    def truncat_model(self) -> Any:
        self.model.truncate()

    @abc.abstractmethod
    def get_elements(self) -> None:
        pass

    @abc.abstractmethod
    def post_save(self, instance) -> None:
        pass

    def sync_information(self) -> None:
        for element in self.get_elements():
            try:
                instance = self.save_information(element)
                self.post_save(instance)
                self.stast["amount_sucessful"] += 1
            except Exception as e:
                logger.error(e)
                self.stast["amount_error"] += 1
    
    @transaction.atomic
    def save_information(self, element: Any) -> None:
        payload = {}
        for property in self.model._meta.get_fields():
            if property.name != "id" and hasattr(element, property.name):
                payload[property.name] = getattr(element, property.name)
        instance = self.model(**payload)
        instance.save()

    def get_stast(self) -> dict:
        return self.stast
