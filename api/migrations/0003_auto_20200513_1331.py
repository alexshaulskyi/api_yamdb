# Generated by Django 3.0.6 on 2020-05-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200513_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
