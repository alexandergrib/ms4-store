# Generated by Django 3.2.9 on 2021-11-29 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211128_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='review_score',
            field=models.PositiveIntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]