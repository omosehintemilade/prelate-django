# Generated by Django 3.0.5 on 2020-12-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acctmang', '0004_auto_20201213_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
