# Generated by Django 3.2.15 on 2022-09-13 11:19

import cloudinary.models
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
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=200, unique=True)),
                ('course_type', models.CharField(choices=[('Starters', 'Starters'), ('Main courses', 'Main courses'), ('Deserts', 'Deserts')], default='Main courses', max_length=12)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_week', models.CharField(choices=[('Current week', 'This week'), ('Next week', 'Next week')], default='Current week', max_length=12)),
                ('booking_day', models.CharField(choices=[('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], default='Tue', max_length=10)),
                ('booking_time', models.CharField(choices=[('17.00-18.30', '17.00-18.30'), ('18.30-20.00', '18.30-20.00'), ('20.00-21.30', '20.00-21.30')], default='17.00-18.30', max_length=20)),
                ('booking_made', models.DateTimeField(auto_now_add=True)),
                ('number_of_guests', models.CharField(choices=[('One guest', 'One guest'), ('Two guests', 'Two guests'), ('Three guests', 'Three guests'), ('Four guests', 'Four guests'), ('Five guests', 'Five guests'), ('Six guests', 'Six guests'), ('Seven guests', 'Seven guests'), ('Eight guests', 'Eight guests')], default='Two guests', max_length=20)),
                ('allergies', models.TextField(blank=True, max_length=50, verbose_name='Allergies')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('booking_week', 'booking_day', 'booking_time'),
                'unique_together': {('guest', 'booking_day', 'booking_time')},
            },
        ),
    ]
