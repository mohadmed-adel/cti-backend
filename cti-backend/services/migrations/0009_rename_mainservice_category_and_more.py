# Generated by Django 5.0.3 on 2024-03-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_mainservice_image_alter_service_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MainService',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='main_service',
            new_name='category',
        ),
    ]
