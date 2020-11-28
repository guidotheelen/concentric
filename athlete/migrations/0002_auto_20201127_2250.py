# Generated by Django 3.0.10 on 2020-11-27 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athlete', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athelete',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to=settings.AUTH_USER_MODEL, verbose_name='Athelete'),
        ),
    ]
