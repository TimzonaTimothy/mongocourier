# Generated by Django 3.0.5 on 2021-09-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0005_auto_20210910_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='agent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='carrier',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='carrier_reference_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='courier',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='destination',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='expected_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='mode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='origin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='payment_mode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='product_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='reciever_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='reciever_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='reciever_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='reciever_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='weight',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]