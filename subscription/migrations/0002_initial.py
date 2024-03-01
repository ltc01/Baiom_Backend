# Generated by Django 4.2 on 2024-03-01 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("subscription", "0001_initial"),
        ("userauths", "0001_initial"),
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchasecourse",
            name="dashboard_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userauths.dashboard_user",
            ),
        ),
        migrations.AddField(
            model_name="purchasecourse",
            name="purchased_course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.course",
            ),
        ),
        migrations.AddField(
            model_name="purchasecourse",
            name="subscription_plan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="subscription.subscriptionplan",
            ),
        ),
    ]
