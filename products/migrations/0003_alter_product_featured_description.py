# Generated by Django 3.2.9 on 2021-12-22 17:54

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211212_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_description',
            field=tinymce.models.HTMLField(blank=True, default='', max_length=400, verbose_name='Featured description max length 400'),
        ),
    ]
