# Generated by Django 4.2.1 on 2023-06-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_images_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pin_top',
            field=models.BooleanField(default=True),
        ),
    ]
