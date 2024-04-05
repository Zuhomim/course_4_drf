# Generated by Django 5.0.3 on 2024-04-05 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('date', models.DateField(blank=True, null=True, verbose_name='дата')),
                ('date_time', models.TimeField(blank=True, default='10:00:00', null=True, verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('periodicity', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение')),
                ('action_time', models.IntegerField(verbose_name='время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]