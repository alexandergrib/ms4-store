# Generated by Django 3.2.9 on 2021-12-05 17:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_featured_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_description',
            field=tinymce.models.HTMLField(default='', max_length=1550),
        ),
    ]
