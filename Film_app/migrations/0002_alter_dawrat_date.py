# Generated by Django 4.1.6 on 2023-02-10 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Film_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dawrat',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]