# Generated by Django 5.2 on 2025-05-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_academicexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicexperience',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='formaciones/'),
        ),
    ]
