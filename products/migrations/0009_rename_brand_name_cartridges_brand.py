# Generated by Django 3.2.9 on 2021-11-30 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_brand_name_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartridges',
            old_name='brand_name',
            new_name='brand',
        ),
    ]
