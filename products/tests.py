from django.test import TestCase
from .models import (Category, Product)


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="laser", friendly_name="Laser")


    def test_category(self):
        """Test Category is created succesfuly"""
        category = Category.objects.get(name="laser")
        self.assertEqual(category.get_friendly_name(), 'Laser')
        
