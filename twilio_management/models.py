import abc
import logging
from django.db import connection, models

logger = logging.getLogger(__name__)
class AbstractModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            logger.info(f"truncate table {cls._meta.db_table}")
            cursor.execute("TRUNCATE TABLE {} CASCADE".format(cls._meta.db_table))

class CustomerProfile(AbstractModel):
    empty = models.BooleanField(default=False)
    # valid_until = models.CharField(max_length=100, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    friendly_name = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)   
    date_created = models.DateTimeField(auto_now_add=False)
    sid = models.CharField(max_length=255, null=True)   
    policy_sid = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True) 
    status_callback = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=16, null=True)

class A2PBrand(AbstractModel):
    date_created = models.DateTimeField(auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=255, null=True)
    friendly_name = models.CharField(max_length=255, null=True)
    # links: Links
    policy_sid = models.CharField(max_length=255, null=True)
    sid = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    status_callback = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    valid_until = models.CharField(max_length=255, null=True)

class BrandRegistration(AbstractModel):
    a2p_brand = models.ForeignKey(
        A2PBrand, on_delete=models.CASCADE, null=True
    )
    a2p_profile_bundle_sid = models.CharField(max_length=64)
    brand_score: models.IntegerField(default=0)
    brand_type: models.CharField(max_length=64)
    customer_profile_bundle_sid = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=True)
    failure_reason = models.CharField(max_length=255, null=True)
    identity_status = models.CharField(max_length=64, null=True)
    mock = models.BooleanField(default=False)
    russell_3000 = models.CharField(max_length=64, null=True)
    sid = models.CharField(max_length=64)
    skip_automatic_sec_vet = models.BooleanField(default=False)
    status = models.CharField(max_length=64)
    tax_exempt_status = models.CharField(max_length=64, null=True)
    tcr_id = models.CharField(max_length=64, null=True)
    url = models.CharField(max_length=255, null=True)



class MessagingService(AbstractModel):
    sid = models.CharField(max_length=34)
    friendly_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=16)

    inbound_request_url = models.CharField(max_length=255, null=True)
    inbound_method = models.CharField(max_length=4)
    fallback_url = models.CharField(max_length=255, null=True)
    fallback_method = models.CharField(max_length=4)
    status_callback = models.CharField(max_length=255, null=True)
    smart_encoding = models.BooleanField(default=False)
    fallback_to_long_code = models.BooleanField(default=False)
    scan_message_content = models.CharField(max_length=255, null=True)
    usecase = models.CharField(max_length=255)
    us_app_to_person_registered = models.BooleanField(default=False)
    use_inbound_webhook_on_number = models.BooleanField(default=False)

    def __str__(self):
        return self.friendly_name


class Compliance(AbstractModel):

    sid = models.CharField(max_length=34)
    friendly_name = models.CharField(max_length=255)
    has_embedded_phone= models.BooleanField(default=False)
    brand_registration_sid= models.CharField(max_length=34)
    description= models.CharField(max_length=255)
    date_updated= models.DateTimeField(auto_now=True)
    campaign_status= models.CharField(max_length=16)
    campaign_id= models.CharField(max_length=34, null=True)
    is_externally_registered= models.BooleanField(default=False)
    has_embedded_links= models.BooleanField(default=False)
    url= models.CharField(max_length=255)
    sid= models.CharField(max_length=34)
    date_created = models.DateTimeField(auto_now_add=False)
    us_app_to_person_usecase = models.CharField(max_length=255)
    mock = models.BooleanField(default=False)
    messaging_service = models.ForeignKey(
        MessagingService, on_delete=models.CASCADE, null=True
    )


class PhoneNumber(AbstractModel):
    phone_number = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=False)
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
