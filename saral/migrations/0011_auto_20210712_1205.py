# Generated by Django 3.2.5 on 2021-07-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saral', '0010_alter_rating_content_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dob',
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image/'),
        ),
    ]
