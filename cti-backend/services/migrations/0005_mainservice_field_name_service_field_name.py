# Generated by Django 5.0.3 on 2024-03-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20240324_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainservice',
            name='field_name',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='service',
            name='field_name',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]