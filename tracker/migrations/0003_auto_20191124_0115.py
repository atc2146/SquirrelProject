# Generated by Django 2.2.7 on 2019-11-24 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20191124_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='ate',
            new_name='date',
        ),
    ]
