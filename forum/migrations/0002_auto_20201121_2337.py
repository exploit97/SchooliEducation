# Generated by Django 3.1.1 on 2020-11-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='title',
            field=models.CharField(default='reponse', max_length=60),
        ),
    ]
