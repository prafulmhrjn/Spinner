# Generated by Django 4.0.3 on 2022-04-17 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_dateandslot_payment_completed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dateandslot',
            name='payment_completed',
        ),
        migrations.RemoveField(
            model_name='dateandslot',
            name='payment_method',
        ),
    ]
