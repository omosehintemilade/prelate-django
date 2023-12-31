# Generated by Django 3.0.5 on 2023-10-08 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='country_of_destination',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='country_of_origin',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='email',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='enquiry',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='relationship',
            name='applicant',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='base.VisaAssistance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='city',
            field=models.CharField(default='jffjf', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='country',
            field=models.CharField(default='dhhd', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='current_employment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='current_relationship_status',
            field=models.CharField(choices=[('SINGLE', 'SINGLE'), ('ENGAGED', 'ENGAGED'), (
                'MARRIED', 'MARRIED'), ('DIVORCED', 'DIVORCED')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='date_of_marriage',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='gender',
            field=models.CharField(
                choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='marital_status',
            field=models.CharField(choices=[('SINGLE', 'SINGLE'), ('ENGAGED', 'ENGAGED'), (
                'MARRIED', 'MARRIED'), ('DIVORCED', 'DIVORCED')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='permanent_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='state',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
