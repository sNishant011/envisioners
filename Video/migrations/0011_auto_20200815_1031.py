# Generated by Django 3.1 on 2020-08-15 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0010_auto_20200815_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_title', models.CharField(max_length=100)),
                ('paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=2048)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Video.description')),
            ],
            options={
                'ordering': ['video_title'],
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
