# Generated by Django 4.2.5 on 2024-04-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FA_overview", "0005_profile_profile_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
