# Generated by Django 3.0.5 on 2023-10-07 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20231002_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaAssistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('SINGLE', 'SINGLE'), ('ENGAGED', 'ENGAGED'), ('MARRIED', 'MARRIED'), ('DIVORCED', 'DIVORCED')], max_length=20)),
                ('dob', models.DateField()),
                ('tribe', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=200)),
                ('postal_address', models.CharField(max_length=200)),
                ('alt_phone_number', models.CharField(max_length=100)),
                ('passport_number', models.CharField(max_length=100)),
                ('date_of_issue', models.DateField()),
                ('date_of_expiry', models.DateField()),
                ('travel_history', models.TextField()),
                ('datetime_of_entry', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Visa Assistance',
                'verbose_name_plural': 'Visa Assistance',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('phonenumber', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('enquiry', models.TextField()),
                ('datetime_of_entry', models.DateTimeField(auto_now_add=True)),
                ('country_of_destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='visa_assistance_destination', to='base.CoveredCountry')),
                ('country_of_origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='visa_assistance_origin', to='base.CoveredCountry')),
            ],
            options={
                'verbose_name': 'Relationship',
                'verbose_name_plural': 'Relationships',
            },
        ),
    ]
