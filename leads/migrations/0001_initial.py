# Generated by Django 3.1.4 on 2022-08-01 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djcrm.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('specialty', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15, null=True, validators=[djcrm.helpers.all_is_digit])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='lead_pfps')),
                ('date_added', models.DateField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leads.category')),
            ],
        ),
        migrations.CreateModel(
            name='LeadPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outlet_geolocation_url', models.URLField(null=True)),
                ('outlet_name', models.CharField(max_length=50, null=True)),
                ('outlet_description', models.TextField(null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leads.lead')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TargetProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='target_product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(null=True)),
                ('agent_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.leadplan')),
            ],
        ),
        migrations.AddConstraint(
            model_name='lead',
            constraint=models.CheckConstraint(check=models.Q(('email__isnull', False), ('phone__isnull', False), _connector='OR'), name='lead_email_or_phone_not_null'),
        ),
    ]
