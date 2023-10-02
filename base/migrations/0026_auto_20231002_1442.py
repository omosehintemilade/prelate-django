# Generated by Django 3.0.5 on 2023-10-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20230823_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=100)),
                ('session_date', models.DateField()),
                ('session_time', models.TimeField()),
                ('datetime_of_entry', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Consultation',
                'verbose_name_plural': 'Consultations',
            },
        ),
        migrations.AlterModelOptions(
            name='travelbudget',
            options={'verbose_name': 'Travel Budget', 'verbose_name_plural': 'Travel Budgets'},
        ),
        migrations.AlterModelOptions(
            name='travelinformation',
            options={'verbose_name': 'Travel Information', 'verbose_name_plural': 'Travel Informations'},
        ),
        migrations.AlterField(
            model_name='coveredcountry',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='countries/'),
        ),
        migrations.AlterField(
            model_name='tourdeal',
            name='deal_image',
            field=models.ImageField(upload_to='tours/'),
        ),
        migrations.AlterField(
            model_name='travelassistance',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='travels/'),
        ),
    ]
