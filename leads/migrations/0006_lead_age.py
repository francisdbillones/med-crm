# Generated by Django 3.1.4 on 2022-08-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20220807_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
