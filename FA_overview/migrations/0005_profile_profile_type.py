# Generated by Django 4.2.5 on 2024-04-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FA_overview", "0004_beep_remove_stockdata_ticker_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_type",
            field=models.CharField(
                blank=True,
                choices=[("Investor", "Investor"), ("Entrepreneur", "Entrepreneur")],
                max_length=20,
                null=True,
            ),
        ),
    ]
