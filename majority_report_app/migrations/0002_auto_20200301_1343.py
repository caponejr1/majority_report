# Generated by Django 2.2.6 on 2020-03-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majority_report_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car1_prog', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Vehicle 1 Progress:')),
                ('ghost_prog', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='AI Ghost Progress:')),
                ('car2_prog', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Vehicle 2 Progress:')),
                ('car1_turndist', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Vehicle 1 Turn Distance:')),
                ('ghost_turndist', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='AI Ghost Turn Distance:')),
                ('car2_turndist', models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Vehicle 2 Turn Distance:')),
            ],
        ),
        migrations.CreateModel(
            name='Enviornment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(verbose_name='Distance:')),
                ('car1_spd', models.IntegerField(verbose_name='Vehicle 1 Speed:')),
                ('car2_spd', models.IntegerField(verbose_name='Vehicle 2 Speed:')),
                ('road_width', models.IntegerField(verbose_name='Road Width:')),
                ('outcome', models.CharField(max_length=120, verbose_name='Outcome:')),
                ('accuracy', models.IntegerField(verbose_name='Accuracy:')),
                ('weather', models.CharField(max_length=120, verbose_name='Weather:')),
                ('time', models.CharField(max_length=120, verbose_name='Time:')),
                ('road_type', models.CharField(max_length=120, verbose_name='Road Type:')),
                ('driver_exp1', models.CharField(max_length=120, verbose_name='Driver 1 Experience:')),
                ('driver_exp2', models.CharField(max_length=120, verbose_name='Driver 2 Experience:')),
                ('driver_dui1', models.CharField(max_length=120, verbose_name='Driver 2 Chemical Influence:')),
                ('driver_vision1', models.CharField(max_length=120, verbose_name='Driver 1 Vision:')),
                ('driver_vision2', models.CharField(max_length=120, verbose_name='Driver 2 Vision:')),
                ('driver_age1', models.CharField(max_length=120, verbose_name='Driver 1 Age:')),
                ('driver_age2', models.CharField(max_length=120, verbose_name='Driver 2 Age:')),
                ('vehicle1', models.CharField(max_length=120, verbose_name='Vehicle 1 Type:')),
                ('vehicle2', models.CharField(max_length=120, verbose_name='Vehicle 2 Type:')),
                ('computer', models.CharField(max_length=120, verbose_name='AI Computer:')),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AddField(
            model_name='drive',
            name='env',
            field=models.ForeignKey(on_delete=models.CASCADE, to='majority_report_app.Enviornment'),
        ),
    ]
