# Generated by Django 3.0.5 on 2023-10-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_auto_20231009_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.CharField(max_length=200)),
                ('disablility', models.CharField(max_length=200)),
                ('past_visa_refusal', models.TextField(null=True)),
                ('other_important_information', models.TextField(null=True)),
                ('extra_curicular_activity', models.TextField(max_length=200)),
                ('datetime_of_entry', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.VisaAssistance')),
            ],
            options={
                'verbose_name': 'Other Information',
                'verbose_name_plural': 'Other Information',
            },
        ),
        migrations.CreateModel(
            name='ApplicationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_not_listed', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('alternative_course', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('datetime_of_entry', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.VisaAssistance')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applicant_country_of_choice', to='base.CoveredCountry')),
            ],
            options={
                'verbose_name': 'Application Information',
                'verbose_name_plural': 'Application Information',
            },
        ),
    ]
