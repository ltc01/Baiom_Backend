# Generated by Django 4.2 on 2024-02-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_wep_title_alter_wep_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wep',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
