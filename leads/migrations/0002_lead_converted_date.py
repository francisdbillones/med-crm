# Generated by Django 3.1.4 on 2022-08-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateField(null=True),
        ),
    ]
