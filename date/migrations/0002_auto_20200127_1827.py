# Generated by Django 3.0.2 on 2020-01-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onl',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='onl',
            name='death',
        ),
        migrations.RemoveField(
            model_name='onl',
            name='event',
        ),
        migrations.AlterField(
            model_name='onl',
            name='date',
            field=models.DateField(unique_for_date=True, verbose_name='날짜'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200, verbose_name='사건')),
                ('year', models.IntegerField(verbose_name='연도')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='date.Onl', verbose_name='날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('year', models.IntegerField(verbose_name='연도')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='date.Onl', verbose_name='날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('year', models.IntegerField(verbose_name='연도')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='date.Onl', verbose_name='날짜')),
            ],
        ),
    ]
