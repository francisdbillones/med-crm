# Generated by Django 4.0.6 on 2022-07-22 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('specialty', models.CharField(max_length=100, null=True)),
                ('office_latitude', models.FloatField(null=True)),
                ('office_longitude', models.FloatField(null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='client_pfps')),
            ],
        ),
        migrations.CreateModel(
            name='ClientPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outlet_latitude', models.FloatField(blank=True, null=True)),
                ('outlet_longitude', models.FloatField(blank=True, null=True)),
                ('outlet_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(blank=True, default=False)),
                ('tuesday', models.BooleanField(blank=True, default=False)),
                ('wednesday', models.BooleanField(blank=True, default=False)),
                ('thursday', models.BooleanField(blank=True, default=False)),
                ('friday', models.BooleanField(blank=True, default=False)),
                ('satuday', models.BooleanField(blank=True, default=False)),
                ('sunday', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TargetProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='target_product_images')),
            ],
        ),
        migrations.AddConstraint(
            model_name='targetproduct',
            constraint=models.CheckConstraint(check=models.Q(('price__isnull', False), ('price__gte', 0)), name='target_product_price_positive'),
        ),
        migrations.AddField(
            model_name='clientplan',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AddField(
            model_name='clientplan',
            name='programs',
            field=models.ManyToManyField(to='clients.program'),
        ),
        migrations.AddField(
            model_name='clientplan',
            name='representative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientplan',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.schedule'),
        ),
        migrations.AddConstraint(
            model_name='client',
            constraint=models.CheckConstraint(check=models.Q(('email__isnull', False), ('phone__isnull', False), _connector='OR'), name='client_email_or_phone_not_null'),
        ),
    ]
