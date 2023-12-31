# Generated by Django 3.0.5 on 2023-10-23 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_merge_20231023_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='postarrivalservice',
            name='time_of_arrival',
            field=models.TimeField(default='12:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postarrivalservice',
            name='accomodation_type',
            field=models.CharField(choices=[('SHARED', 'Shared Apartment'), ('STUDIO', 'Studio Apartment'), ('2 BEDROOM', '2 Bedroom Apartment')], max_length=200),
        ),
        migrations.AlterField(
            model_name='postarrivalservice',
            name='approved_visa_type',
            field=models.CharField(choices=[('STUDENT VISA', 'Student Visa'), ('WORK VISA', 'Work Visa'), ('TOURIST VISA', 'Tourist Visa'), ('BUSINESS VISA', 'Business Visa')], max_length=200),
        ),
    ]
