from django.contrib import admin

from twilio_management.models import Compliance, MessagingService, PhoneNumber


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(MessagingService)
class MessagingServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    pass
