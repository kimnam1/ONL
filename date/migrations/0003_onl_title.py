# Generated by Django 3.0.2 on 2020-01-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0002_auto_20200127_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='onl',
            name='title',
            field=models.CharField(blank=True, max_length=20, verbose_name='제목 날짜'),
        ),
    ]