# Generated by Django 3.0.5 on 2023-01-24 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0014_auto_20230124_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='comments',
        ),
    ]
