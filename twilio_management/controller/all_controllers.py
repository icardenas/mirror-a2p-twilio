from twilio_management.controller.abstract_controller import AbstractController
from typing import Iterator


class PhoneNumberController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.incoming_phone_numbers.stream()

    def post_save(self, instance) -> None:
        pass


class MessagingServicesController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.messaging.services.stream()

    def post_save(self, instance) -> None:
        pass
