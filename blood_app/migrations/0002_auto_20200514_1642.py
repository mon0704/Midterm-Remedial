# Generated by Django 2.2 on 2020-05-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestblood',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
