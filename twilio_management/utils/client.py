import logging
import os
from typing import Dict

from twilio.rest import Client


class TwilioClient:
    def __init__(self):
        self.connection = self.get_twilio_connection()
        self.error: str = None
        self.stats: dict = {"successful": False}

    def get_twilio_connection(self):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        return Client(account_sid, auth_token)
