# Generated by Django 4.0.1 on 2022-02-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0010_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='dctr',
            name='prc',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='dctr',
            name='prccherg',
            field=models.CharField(default='', max_length=25),
        ),
    ]
