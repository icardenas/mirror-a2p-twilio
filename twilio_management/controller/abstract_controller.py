import abc
from typing import Any
from twilio_management.utils.client import TwilioClient


class AbstractController(abc.ABC):

    def __init__(self, model: Any) -> None:
        self.twilio_client = TwilioClient()
        self.stast:dict = {'amount_sucessful': 0, 'amount_error': 0}
        self.model = model
        self.truncat_model()
        
    def truncat_model(self) -> Any:
        self.model.truncate()

    @abc.abstractmethod
    def get_elements(self) -> None:
        pass

    def sync_information(self) -> None:
        for element in self.get_elements():
            try:
                self.save_information(element)
                self.stast['amount_sucessful'] += 1
            except Exception as e:
                self.stast['amount_error'] += 1

    def save_information(self, element: Any) -> None:
        payload = {}
        for property in self.model.__attributes__:
            if property != 'id':
                payload[property] = getattr(element, property)
        new_object = self.model(**payload)
        new_object.save()

    def get_stast(self) -> dict:
        return self.stast
    