# Generated by Django 4.0.1 on 2022-02-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0015_alter_patient_currentstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
