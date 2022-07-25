# Generated by Django 3.0.3 on 2020-03-02 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateAndSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('booking_slot', models.TextField(choices=[('Slot 1', 'S1'), ('Slot 2', 'S2')])),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('chosen_date_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.DateAndSlot')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms_available', models.IntegerField(null=True)),
                ('booking_date_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.DateAndSlot')),
            ],
        ),
    ]
