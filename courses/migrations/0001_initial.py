# Generated by Django 3.1.1 on 2020-10-01 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(default='cat_images/default.jpg', upload_to='cat_images')),
            ],
        ),
        migrations.CreateModel(
            name='Sujets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('course_image', models.ImageField(default='default.jpg', upload_to='kurs_images')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.classe')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=11)),
                ('position', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.sujets')),
            ],
        ),
    ]
