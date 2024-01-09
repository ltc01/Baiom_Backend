# Generated by Django 4.2.9 on 2024-01-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Web Development', 'Web Development'), ('Data Analyst', 'Data Analyst'), ('Data Science', 'Data Science'), ('Content Writing', 'Content Writing'), ('Graphic Designing', 'Graphic Designing'), ('SEO Marketing', 'SEO Marketing'), ('Digital Marketing', 'Digital Marketing'), ('Project Management', 'Project Management'), ('Human Resources', 'Human Resources'), ('Corporation', 'Corporation')], default='Web Development', max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('draft', 'Draft')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
