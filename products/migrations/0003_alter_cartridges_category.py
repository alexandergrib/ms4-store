# Generated by Django 3.2.9 on 2021-12-05 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cartridges_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridges',
            name='category',
            field=models.ForeignKey(blank=True, default='cartridges', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
