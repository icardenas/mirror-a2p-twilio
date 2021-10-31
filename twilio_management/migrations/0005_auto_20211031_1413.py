# Generated by Django 3.2.8 on 2021-10-31 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_management', '0004_auto_20211031_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliance',
            name='brand_registration_sid',
            field=models.CharField(default='', max_length=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliance',
            name='campaign_id',
            field=models.CharField(default='', max_length=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliance',
            name='campaign_status',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliance',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='compliance',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliance',
            name='has_embedded_links',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='compliance',
            name='has_embedded_phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='compliance',
            name='is_externally_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='compliance',
            name='url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]