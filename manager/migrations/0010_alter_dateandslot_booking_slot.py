# Generated by Django 4.0.3 on 2022-04-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_alter_dateandslot_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateandslot',
            name='booking_slot',
            field=models.TextField(choices=[('Slot 1', 'S1'), ('Slot 2', 'S2')], max_length=7),
        ),
    ]