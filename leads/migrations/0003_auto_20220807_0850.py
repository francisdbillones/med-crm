# Generated by Django 3.1.4 on 2022-08-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_converted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=models.TextField(blank=True, default='No description'),
        ),
    ]
