# Generated by Django 4.1.6 on 2023-02-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film_app', '0005_offre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='status',
            field=models.CharField(blank=True, choices=[('Pro', 'Pro'), ('Enterprise', 'Enterprise')], max_length=50, null=True),
        ),
    ]
