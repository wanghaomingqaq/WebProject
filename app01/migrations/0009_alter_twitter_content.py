# Generated by Django 3.2.1 on 2021-05-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter',
            name='content',
            field=models.CharField(max_length=256),
        ),
    ]
