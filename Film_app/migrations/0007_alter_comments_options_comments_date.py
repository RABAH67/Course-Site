# Generated by Django 4.1.6 on 2023-02-11 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Film_app', '0006_alter_offre_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]