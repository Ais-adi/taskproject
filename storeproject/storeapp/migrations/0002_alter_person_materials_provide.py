# Generated by Django 3.2.15 on 2023-01-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='materials_provide',
            field=models.CharField(max_length=255),
        ),
    ]
