# Generated by Django 3.0.5 on 2020-08-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20200803_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelassistance',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/travels'),
        ),
    ]
