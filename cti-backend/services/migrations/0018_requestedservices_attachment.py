# Generated by Django 5.0.3 on 2024-04-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedservices',
            name='attachment',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
