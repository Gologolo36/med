# Generated by Django 4.0.1 on 2022-02-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0009_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
