# Generated by Django 5.0.6 on 2024-06-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
