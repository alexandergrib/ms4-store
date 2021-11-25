from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    specifications = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReviews(models.Model):

    class Meta:
        verbose_name_plural = 'Product Reviews'

    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    # order = models.ForeignKey('Order', on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    review_title = models.CharField(max_length=254, null=True, blank=True)
    review_text = models.CharField(max_length=1024, null=True, blank=True)
    review_image = models.ImageField(null=True, blank=True)
    review_score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.product.name + "_" + str(self.review_score)


class ProductImages(models.Model):

    class Meta:
        verbose_name_plural = 'Product Images'

    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
