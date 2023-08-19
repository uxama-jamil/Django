# Generated by Django 4.2.4 on 2023-08-19 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolsys.teacher')),
            ],
        ),
    ]