# Generated by Django 3.2.1 on 2021-05-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_qidian'),
    ]

    operations = [
        migrations.AddField(
            model_name='qidian',
            name='rank',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
