from django.db import models


class MessagingService(models.Model):
    sid = models.CharField(max_length=34)
    friendly_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16)

    inbound_request_url = models.CharField(max_length=255)
    inbound_method = models.CharField(max_length=4)
    fallback_url = models.CharField(max_length=255)
    fallback_method = models.CharField(max_length=4)
    status_callback = models.CharField(max_length=255)
    smart_encoding = models.BooleanField(default=False)
    fallback_to_long_code = models.BooleanField(default=False)
    scan_message_content = models.CharField(max_length=255)
    usecase = models.CharField(max_length=255)
    us_app_to_person_registered = models.BooleanField(default=False)
    use_inbound_webhook_on_number = models.BooleanField(default=False)

    def __str__(self):
        return self.friendly_name


class Compliance(models.Model):

    sid = models.CharField(max_length=34)
    friendly_name = models.CharField(max_length=255)
    has_embedded_phone: models.BooleanField(default=False)
    brand_registration_sid: models.CharField(max_length=34)
    description: models.CharField(max_length=255)
    # message_samples: List[str]
    date_updated: models.DateTimeField(auto_now=True)
    campaign_status: models.CharField(max_length=16)
    # rate_limits:
    campaign_id: models.CharField(max_length=34)
    is_externally_registered: models.BooleanField(default=False)
    has_embedded_links: models.BooleanField(default=False)
    url: models.CharField(max_length=255)
    sid: models.CharField(max_length=34)
    date_created = models.DateTimeField(auto_now_add=True)
    us_app_to_person_usecase = models.CharField(max_length=255)
    mock = models.BooleanField(default=False)
    messaging_service = models.ForeignKey(
        MessagingService, on_delete=models.CASCADE, null=True
    )


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sid = models.CharField(max_length=34)
    sms_fallback_method = models.CharField(max_length=4)
    sms_fallback_url = models.CharField(max_length=255)
    sms_method = models.CharField(max_length=4)
    sms_url = models.CharField(max_length=255)
    status_callback = models.CharField(max_length=255)
    status_callback_method = models.CharField(max_length=4)
    status = models.CharField(max_length=16)
    messaging_service = models.ForeignKey(
        MessagingService, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.friendly_name
