# Generated by Django 3.1.1 on 2020-10-16 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Concours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='image/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.category')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nom')),
                ('solution_file', models.FileField(upload_to='solutions')),
                ('price', models.CharField(max_length=30)),
                ('creator', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom')),
                ('subject_file', models.FileField(blank=True, null=True, upload_to='sujects')),
                ('country', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.country')),
                ('etablissement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.etablissement')),
                ('examen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.concours')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.level')),
                ('matter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.matter')),
                ('solution', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.solution')),
                ('year', models.ForeignKey(default=2014, on_delete=django.db.models.deletion.CASCADE, to='examen_et_concours.year')),
            ],
        ),
    ]
