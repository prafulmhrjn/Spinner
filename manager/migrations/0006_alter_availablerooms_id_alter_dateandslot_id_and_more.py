# Generated by Django 4.0.3 on 2022-04-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_dateandslot_rooms_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablerooms',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dateandslot',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
