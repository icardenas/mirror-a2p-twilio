from django.contrib import admin

from twilio.models import Compliance, MessagingService, PhoneNumber
from django.contrib import admin


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(MessagingService)
class MessagingServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    pass
