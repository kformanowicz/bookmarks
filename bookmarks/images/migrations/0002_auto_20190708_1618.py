# Generated by Django 2.2.2 on 2019-07-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='blank.png', null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]