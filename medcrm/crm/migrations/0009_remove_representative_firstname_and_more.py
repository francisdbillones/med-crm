# Generated by Django 4.0.6 on 2022-07-19 06:49

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_alter_client_email_alter_client_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representative',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='representative',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='representative',
            name='password',
            field=models.CharField(default=None, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='representative',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]