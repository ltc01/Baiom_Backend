# Generated by Django 4.2 on 2024-03-22 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_dashboard_user_enrolled_bootbatches_and_more'),
        ('itie', '0002_icourse_plus_icourse_premium'),
        ('subscription', '0004_subscriptionplancourse_course_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseItie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('plans_duration_months', models.PositiveIntegerField(editable=False)),
                ('purchase_start_date', models.DateField()),
                ('purchase_end_date', models.DateField()),
                ('additional_access_date', models.DateField()),
                ('Batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itie.ibatch')),
                ('dashboard_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userauths.dashboard_user')),
                ('purchased_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itie.icourse')),
                ('subscription_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subscription.subscriptionplan')),
            ],
        ),
    ]
