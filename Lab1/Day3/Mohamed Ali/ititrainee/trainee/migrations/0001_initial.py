# Generated by Django 4.0.5 on 2022-06-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationalnum', models.IntegerField(null=True)),
                ('branch', models.IntegerField(null=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainee.course')),
            ],
        ),
    ]