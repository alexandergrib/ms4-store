# Most of the testing code was used from https://github.com/Abibubble/ms4-lead-shot-hazard/ with adaptation to suit my project

from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from .models import Category, Product, Cartridges


class TestProductViews(TestCase):
    """
    Test that the product views work as expected
    """

    fixtures = [
        'fixtures.json',
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')

    def test_the_products_page_url_exists(self):
        """
        Test that the products page URL exists
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_the_products_url_is_accessible_by_name(self):
        """
        Test that the products page is accessible via name
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products_view_uses_correct_template(self):
        """
        Test that the products page uses the correct template
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='products/products.html')

    def test_products(self):
        """
        Test that a product can be retrieved
        """
        products = Product.objects.all()
        for product in products:
            response = self.client.get(reverse('products'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, product.pk)

    def test_categories(self):
        """
        Test that the category sort feature works as expected
        """
        product = Product.objects.get(
            id='679d1833-a1b5-4120-87ee-2afcedd50cf6')
        category = Category.objects.get(pk=2)
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.category, category)
        self.assertContains(response, product.category)


    def test_product_detail(self):
        """
        Test that a product detail can be retrieved
        """
        product = Product.objects.get(
            id='679d1833-a1b5-4120-87ee-2afcedd50cf6')
        response = self.client.get(reverse('products'))
        self.assertContains(response, product.name)

    def test_cartridge_detail(self):
        """
        Test that a cartridge detail can be retrieved
        """
        product = Cartridges.objects.get(
            id='76d01792-8853-4e62-bd6f-01d9140dc97f')
        response = self.client.get(reverse('product_detail',
                                           args=[product.id]))
        self.assertContains(response, product.model)

    def test_the_product_detail_page_url_exists(self):
        """
        Test that the product detail page URL exists
        """
        response = self.client.get(
            '/products/679d1833-a1b5-4120-87ee-2afcedd50cf6/')
        self.assertEqual(response.status_code, 200)

    def test_the_cartridge_detail_page_url_exists(self):
        """
        Test that the product detail page URL exists
        """
        response = self.client.get(
            '/products/76d01792-8853-4e62-bd6f-01d9140dc97f/')
        self.assertEqual(response.status_code, 200)

    def test_sort_name_functionality(self):
        """
        Test that the sort function works
        """
        category_name = 'laser_printers'
        sort_array = ['name', 'category', 'brand', 'special']
        for sort in sort_array:
            direction = 'desc'
            current_sorting = f'{sort}_{direction}'
            response = self.client.get(
                f'/products/?category={category_name}'
                f'&sort={sort}&direction={direction}')
            self.assertEqual(current_sorting, f'{sort}_desc')
            self.assertEqual(response.status_code, 200)

    def test_product_search_functionality(self):
        """
        Test that the search bar returns what is expected
        """
        response = self.client.get(
            '/products/?', {'q': 'printer'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'printer')

    def test_search_error_messages_output(self):
        """
        Test that the search error message display correctly
        """
        response = self.client.get(
            '/products/?', {'q': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "You didn't enter any search criteria!")
        self.assertEqual(response.status_code, 302)


class TestProductViewsAddData(TestCase):
    """
    Test that the product views work as expected
    """

    fixtures = [
        'fixtures.json',

    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')

    def test_add_product_for_regular_users_view(self):
        """
        Test the add_product view doesn't allow
        non-superusers to access the page
        """
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only store owners can do that.')
        self.assertEqual(response.status_code, 302)

    def test_add_cartridge_for_regular_users_view(self):
        """
        Test the add_product view doesn't allow
        non-superusers to access the page
        """
        self.client.login(
            username='testuser', email='test@test.com',
            password='te12345st')
        response = self.client.get('/products/add/cartridge/243e2262-9d21-4c12-88cb-d0a47ccf66a0')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only store owners can do that.')
        self.assertEqual(response.status_code, 302)

    def test_the_add_product_page_works_for_superuser(self):
        """
        Test that the add_product page works for superuser
        """
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(
            response, template_name='products/add_product.html')

    def test_edit_product_for_regular_users_view(self):
        """
        Test the edit_product view doesn't allow
        non-superusers to access the page
        """
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/product/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    def test_edit_cartridge_for_regular_users_view(self):
        """
        Test the edit_cartridge view doesn't allow
        non-superusers to access the page
        """
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Cartridges.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/cartridge/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    def test_the_edit_product_page_works_for_superuser(self):
        """
        Test that the edit_product page works for superuser
        """
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/product/{product.pk}/')
            self.assertEqual(response.status_code, 200)

    def test_the_edit_cartridge_page_works_for_superuser(self):
        """
        Test that the edit_cartridge page works for superuser
        """
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Cartridges.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/cartridge/{product.pk}/')
            self.assertEqual(response.status_code, 200)

    def test_delete_product_for_regular_users_view(self):
        """
        Test the delete_product view doesn't allow
        non-superusers to access the page
        """
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    def test_delete_cartridge_for_regular_users_view(self):
        """
        Test the delete_cartridge view doesn't allow
        non-superusers to access the page
        """
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Cartridges.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/cartridge/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    def test_the_delete_product_page_works_for_superuser(self):
        """
        Test that the delete_product page works for superuser
        """
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/{product.pk}/')
            self.assertEqual(response.status_code, 302)

    def test_the_delete_cartridge_page_works_for_superuser(self):
        """
        Test that the delete_cartridge page works for superuser
        """
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Cartridges.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/cartridge/{product.pk}/')
            self.assertEqual(response.status_code, 302)
