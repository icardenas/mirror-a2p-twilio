# Generated by Django 3.2.8 on 2022-11-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_management', '0008_alter_compliance_campaign_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandregistration',
            name='brand_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='brandregistration',
            name='brand_type',
            field=models.CharField(null=True, max_length=64),
            preserve_default=False,
        )
    ]
