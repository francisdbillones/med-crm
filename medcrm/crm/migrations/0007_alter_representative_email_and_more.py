# Generated by Django 4.0.6 on 2022-07-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_representative_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='representative_pfps'),
        ),
        migrations.AlterField(
            model_name='representative',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]