# Generated by Django 4.1.6 on 2023-02-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film_app', '0002_alter_dawrat_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dawrat',
            name='description_detail',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]