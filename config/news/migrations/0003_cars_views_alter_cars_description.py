# Generated by Django 5.1.4 on 2024-12-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_cars_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
