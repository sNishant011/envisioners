# Generated by Django 3.1 on 2020-08-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0018_auto_20200819_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideo',
            name='background_image',
            field=models.CharField(max_length=2048),
        ),
    ]
