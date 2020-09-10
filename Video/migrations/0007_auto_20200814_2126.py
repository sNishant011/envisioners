# Generated by Django 3.1 on 2020-08-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0006_auto_20200814_2122'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.AlterField(
            model_name='categories',
            name='parent',
            field=models.ManyToManyField(blank=True, default=None, related_name='_categories_parent_+', to='Video.Categories'),
        ),
    ]
