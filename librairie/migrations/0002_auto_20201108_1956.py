# Generated by Django 3.1.1 on 2020-11-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librairie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(upload_to='', verbose_name="upload_to='librairie_image', default='default.jpg"),
        ),
    ]
