# Generated by Django 3.2.8 on 2021-11-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_management', '0007_customerprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliance',
            name='campaign_id',
            field=models.CharField(max_length=34, null=True),
        ),
    ]