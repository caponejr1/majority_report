# Generated by Django 2.2.6 on 2020-03-07 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majority_report_app', '0007_remove_drive_iterations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='majority_report_app.Enviornment'),
        ),
    ]
