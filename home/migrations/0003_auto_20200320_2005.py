# Generated by Django 2.2.11 on 2020-03-20 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="hello",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_hello",
                to="home.CustomText",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="sdf",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_sdf",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="test",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_test",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
