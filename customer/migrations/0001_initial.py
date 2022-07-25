# Generated by Django 4.0.3 on 2022-04-16 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0012_alter_dateandslot_booking_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookee_username', models.CharField(default='Admin', max_length=50)),
                ('customer_name', models.CharField(max_length=60)),
                ('customer_email', models.EmailField(max_length=254, unique=True)),
                ('customer_contact', models.CharField(max_length=12, unique=True)),
                ('booking_purpose', models.CharField(blank=True, max_length=254)),
                ('booked_room_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='manager.room')),
                ('booking_date_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.dateandslot')),
            ],
        ),
    ]
