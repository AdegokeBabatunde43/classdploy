# Generated by Django 4.1 on 2022-09-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]