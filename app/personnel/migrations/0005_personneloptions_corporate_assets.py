# Generated by Django 4.1.3 on 2022-11-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_personneloptions_voluntary_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='personneloptions',
            name='corporate_assets',
            field=models.BooleanField(default=False),
        ),
    ]
