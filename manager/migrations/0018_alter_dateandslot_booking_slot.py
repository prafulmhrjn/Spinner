# Generated by Django 4.0.3 on 2022-04-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_remove_dateandslot_payment_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateandslot',
            name='booking_slot',
            field=models.CharField(choices=[('Slot 1', 'Morning : 5 AM'), ('Slot 2', 'Morning : 7 AM'), ('Slot 3', 'Morning : 9 AM'), ('Slot 4', 'Morning : 11 AM'), ('Slot 5', 'Afternoon : 1 PM'), ('Slot 6', 'Afternoon : 3 PM'), ('Slot 7', 'Evening : 5 PM'), ('Slot 8', 'Evening : 7 PM'), ('Slot 9', 'Night : 5 PM')], max_length=225),
        ),
    ]
