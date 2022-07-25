# Generated by Django 4.0.3 on 2022-04-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='roombooking',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Khalti', 'Khalti'), ('Esewa', 'Esewa')], default='Cash', max_length=20),
        ),
    ]