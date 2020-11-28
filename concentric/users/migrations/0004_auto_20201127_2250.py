# Generated by Django 3.0.10 on 2020-11-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201113_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='biological_sex',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fat_percentage',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lenght_cm',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='prefered_units',
        ),
        migrations.RemoveField(
            model_name='user',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight_kg',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]