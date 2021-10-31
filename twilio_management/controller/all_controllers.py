from twilio_management.controller.abstract_controller import AbstractController
from typing import Iterator


class PhoneNumberController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.incoming_phone_numbers.stream()


class MessagingServicesController(AbstractController):
    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.twilio_connection.messaging.services.stream()
