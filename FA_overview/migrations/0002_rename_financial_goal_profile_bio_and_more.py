# Generated by Django 4.2.5 on 2024-04-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FA_overview", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="financial_goal",
            new_name="Bio",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="risk_tolerance",
            new_name="Industry",
        ),
        migrations.AddField(
            model_name="profile",
            name="follows",
            field=models.ManyToManyField(
                blank=True, related_name="followed_by", to="FA_overview.profile"
            ),
        ),
    ]
