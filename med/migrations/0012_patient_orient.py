# Generated by Django 4.0.1 on 2022-02-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0011_dctr_prc_dctr_prccherg'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='orient',
            field=models.CharField(default='', max_length=20),
        ),
    ]
