# Generated by Django 4.2.1 on 2023-05-26 04:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user_month_user_year_alter_user_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="latitude_south",
        ),
        migrations.AddField(
            model_name="user",
            name="latitude",
            field=models.DecimalField(
                decimal_places=2,
                default=51.5,
                max_digits=2,
                verbose_name="Latitude (In degrees)",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date",
            field=models.PositiveIntegerField(
                default=1,
                validators=[
                    django.core.validators.MaxValueValidator(31),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Date",
            ),
        ),
    ]