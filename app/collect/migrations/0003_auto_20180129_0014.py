# Generated by Django 2.0 on 2018-01-29 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Observation datetime')),
                ('bid', models.CharField(max_length=16, verbose_name='Bus ID')),
                ('secsSinceReport', models.IntegerField(default=0)),
                ('lat', models.DecimalField(decimal_places=7, default=0, max_digits=11)),
                ('lon', models.DecimalField(decimal_places=7, default=0, max_digits=11)),
                ('kph', models.IntegerField(default=0)),
                ('heading', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='duration',
        ),
        migrations.AddField(
            model_name='trip',
            name='end_lat',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AddField(
            model_name='trip',
            name='end_lon',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_lat',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_lon',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='route',
            name='rid',
            field=models.CharField(db_index=True, max_length=10, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_datetime',
            field=models.DateTimeField(verbose_name='End of Trip Time'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='ip_address',
            field=models.CharField(db_index=True, max_length=16, unique=True, verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collect.Route'),
        ),
        migrations.AddField(
            model_name='observation',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collect.Trip'),
        ),
    ]
