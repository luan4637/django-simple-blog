# Generated by Django 4.2.1 on 2023-06-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_pin_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pin_top',
            field=models.BooleanField(default=False),
        ),
    ]