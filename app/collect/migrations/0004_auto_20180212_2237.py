# Generated by Django 2.0 on 2018-02-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0003_auto_20180129_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='ip_address',
            field=models.CharField(db_index=True, max_length=16, verbose_name='IP Address'),
        ),
    ]
