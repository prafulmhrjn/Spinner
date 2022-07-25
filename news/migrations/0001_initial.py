# Generated by Django 4.0.3 on 2022-04-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, null=True)),
                ('news_description', models.TextField()),
                ('news_snippets', models.CharField(max_length=255)),
                ('news_publisher', models.CharField(max_length=500)),
            ],
        ),
    ]
