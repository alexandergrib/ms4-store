from django.test import TestCase
from .models import (Category, Product, ProductBrand)
import datetime

# class CategoryTestCase(TestCase):
# databases = {'test_db'}

# def setUp(self):
#     category = Category.objects.get(pk=1)
#     brand = ProductBrand.objects.get(pk=1)
#     product = Product.objects.get(pk='9765521f-1f87-4a75-a894-e50e539841cc')

# def test_product_name(self):
#     """
#     Test that the product name is retrieved correctly
#     """
#     product = Product.objects.get(
#         pk='9765521f-1f87-4a75-a894-e50e539841cc')
#     print(product)
#     self.assertEqual(product.name, 'A4 Mono Laser Printer')
#     # self.assertEqual(1, 1)

# def test_category(self):
#     """Test Category is created successfully"""
#     category = Category.objects.get(pk=1)
#     self.assertEqual(category.get_friendly_name(), 'Laser printers')
#
# def test_brand(self):
#     """Test Brand is created successfully"""
#     brand = ProductBrand.objects.get(pk=1)
#     self.assertEqual(brand.get_friendly_name(), 'Brother')
