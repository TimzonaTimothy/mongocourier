# Generated by Django 3.0.5 on 2022-04-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message_subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]