# Generated by Django 4.2.5 on 2024-04-07 06:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FA_overview", "0002_rename_financial_goal_profile_bio_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modidfied",
            field=models.DateField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]
