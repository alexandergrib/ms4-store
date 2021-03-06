"""
 Most of the testing code was used from
 https://github.com/Abibubble/ms4-lead-shot-hazard/ with adaptation to
 suit my project
"""
from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test that the order form works as expected
    """

    def test_full_name_is_required(self):
        """
        Test if form submits without full_name field completed
        """
        form = OrderForm({
            'full_name': '',
            'email': 'test@email.com',
            'phone_number': '0775624532',
            'street_address1': 'test',
            'street_address2': '',
            'town_or_city': 'test',
            'postcode': '',
            'country': 'GB',
            'county': ''
        })
        # Form should not be valid, as full_name is required
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Test if form submits without email field completed
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '0775624532',
            'street_address1': 'test',
            'street_address2': '',
            'town_or_city': 'test',
            'postcode': '',
            'country': 'GB',
            'county': ''
        })
        # Form should not be valid, as email is required
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        Test if form submits without phone_number field completed
        """
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid, as phone_number is required
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test if form submits without country field completed
        """
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': '',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid, as country is required
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        """
        Test if form submits without town_or_city field completed
        """
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': '',
            'street_address1': 'test',
        })
        # Form should not be valid, as town_or_city is required
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        """
        Test if form submits without street_address1 field completed
        """
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': '',
        })
        # Form should not be valid, as street_address1 is required
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_fields_are_correct_in_meta_class(self):
        """
        Check that the form fields that are visible
        to the user are the correct ones
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        ))
