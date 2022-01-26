# Most of the testing code was used from https://github.com/Abibubble/ms4-lead-shot-hazard/ with adaptation to suit my project
from django.test import TestCase

from .models import Category, Product


class TestProductModels(TestCase):
    """
    Test that the products work as expected
    """

    fixtures = [
        'fixtures.json',
    ]

    def test_product_name(self):
        """
        Test that the product name is retrieved correctly
        """
        product = Product.objects.get(pk='1b6622c4-3fde-4afe-b3bd-673a038454b6')
        self.assertEqual(product.model, 'C235')
        self.assertNotEqual(product.name, 'Test name')


    def test_product_sku(self):
        """
        Test that the product description is retrieved correctly
        """
        product = Product.objects.get(pk='1b6622c4-3fde-4afe-b3bd-673a038454b6')
        self.assertEqual(
            product.sku, "D235V_DNIUK"
        )
        self.assertNotEqual(product.sku, 'test if not equal')



class TestCategoryModels(TestCase):
    """
    Test that the categories work as expected
    """

    fixtures = [
         'fixtures.json',
    ]

    def test_category_name(self):
        """
        Test that the category name is retrieved correctly
        """
        category = Category.objects.get(pk=2)
        self.assertEqual(category.name, 'inkjet_printers')
        self.assertNotEqual(category.name, 'test')
        self.assertEqual(str(category), category.name)

    def test_category_friendly_name(self):
        """
        Test that the category friendly name is retrieved correctly
        """
        category = Category.objects.get(pk=2)
        self.assertEqual(category.friendly_name, 'Inkjet Printers')
        self.assertNotEqual(category.friendly_name, 'Test Category')
        self.assertEqual(
            Category.get_friendly_name(category), category.friendly_name)
