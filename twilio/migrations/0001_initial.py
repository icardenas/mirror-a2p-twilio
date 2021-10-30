# Generated by Django 3.2.8 on 2021-10-30 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessagingService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sid", models.CharField(max_length=34)),
                ("friendly_name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(max_length=16)),
                ("inbound_request_url", models.CharField(max_length=255)),
                ("inbound_method", models.CharField(max_length=4)),
                ("fallback_url", models.CharField(max_length=255)),
                ("fallback_method", models.CharField(max_length=4)),
                ("status_callback", models.CharField(max_length=255)),
                ("smart_encoding", models.BooleanField(default=False)),
                ("fallback_to_long_code", models.BooleanField(default=False)),
                ("scan_message_content", models.CharField(max_length=255)),
                ("usecase", models.CharField(max_length=255)),
                ("us_app_to_person_registered", models.BooleanField(default=False)),
                ("use_inbound_webhook_on_number", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.CharField(max_length=20)),
                ("friendly_name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("sid", models.CharField(max_length=34)),
                ("sms_fallback_method", models.CharField(max_length=4)),
                ("sms_fallback_url", models.CharField(max_length=255)),
                ("sms_method", models.CharField(max_length=4)),
                ("sms_url", models.CharField(max_length=255)),
                ("status_callback", models.CharField(max_length=255)),
                ("status_callback_method", models.CharField(max_length=4)),
                ("status", models.CharField(max_length=16)),
                (
                    "messaging_service",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="twilio.messagingservice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Compliance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sid", models.CharField(max_length=34)),
                ("friendly_name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("us_app_to_person_usecase", models.CharField(max_length=255)),
                ("mock", models.BooleanField(default=False)),
                (
                    "messaging_service",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="twilio.messagingservice",
                    ),
                ),
            ],
        ),
    ]
