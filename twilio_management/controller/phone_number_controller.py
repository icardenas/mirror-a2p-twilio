

from twilio_management.controller.abstract_controller import AbstractController
from typing import Iterator


class PhoneNumberController(AbstractController):

    def get_elements(self) -> Iterator[object]:
        return self.twilio_client.connection.incoming_phone_numbers.stream()
