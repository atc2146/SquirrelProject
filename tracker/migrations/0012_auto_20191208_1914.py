# Generated by Django 2.2.7 on 2019-12-09 00:14

from django.db import migrations, models
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20191207_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(default=None, help_text='date sighted', validators=[tracker.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='', help_text='Time of sighting', max_length=2),
        ),
    ]