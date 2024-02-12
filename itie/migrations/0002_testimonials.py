# Generated by Django 4.2 on 2024-02-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='itie_testimonials')),
                ('name', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
    ]
