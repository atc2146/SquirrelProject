# Generated by Django 2.2.7 on 2019-11-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20191124_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='', help_text='Age of squirrel', max_length=10),
        ),
        migrations.AddField(
            model_name='sighting',
            name='approaches',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='chasing',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='climbing',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='eating',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='foraging',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='indifferent',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='kuks',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='', help_text='Location of where the squirrel was when first sighted', max_length=20),
        ),
        migrations.AddField(
            model_name='sighting',
            name='moans',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='other_activites',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='sighting',
            name='primary_fur_color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], default='', help_text='Fur color of squirrel', max_length=20),
        ),
        migrations.AddField(
            model_name='sighting',
            name='quaas',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='running',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='runs_from',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='specific_location',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='sighting',
            name='tail_flags',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='tail_twitches',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='unique_squirrel_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(verbose_name='date sighted'),
        ),
    ]