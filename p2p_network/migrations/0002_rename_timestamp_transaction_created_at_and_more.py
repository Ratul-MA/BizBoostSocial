# Generated by Django 4.2.5 on 2024-04-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("p2p_network", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="timestamp",
            new_name="created_at",
        ),
        migrations.AddField(
            model_name="transaction",
            name="memo",
            field=models.TextField(blank=True),
        ),
    ]
