# Generated by Django 5.1 on 2024-09-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_alter_tweet_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(),
        ),
    ]