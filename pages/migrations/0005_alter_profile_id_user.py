# Generated by Django 4.1 on 2022-09-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(),
        ),
    ]
