# from django.test import TestCase
# from .forms import (RatingForm, CartrigesForm,
#                     ProductSpecsForm, BrandForm,
#                     CategoryForm, ProductForm
#                     )
#
# class TestRatingForm(TestCase):
#     def test_item_name_is_required(self):
#         form = RatingForm({'name': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('name', form.errors.keys())
#         self.assertEqual(form.errors['name'][0], 'This field is required.')