# Generated by Django 2.2.6 on 2020-02-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=120, verbose_name='Distance:')),
                ('car1_spd', models.CharField(max_length=120, verbose_name='Vehicle 1 Speed:')),
                ('car2_spd', models.CharField(max_length=120, verbose_name='Vehicle 2 Speed:')),
                ('road_width', models.CharField(max_length=120, verbose_name='Road Width:')),
            ],
        ),
    ]
