# Generated by Django 2.2.6 on 2020-03-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majority_report_app', '0005_auto_20200307_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='iterations',
            field=models.IntegerField(default=0, verbose_name='Iterations:'),
        ),
    ]
