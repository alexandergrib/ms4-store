import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from profiles.models import UserProfile
from django.db.models import Avg
from tinymce import models as tinymce_models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Special(models.Model):
    class Meta:
        verbose_name_plural = 'Specials'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductBrand(models.Model):
    brand_name = models.CharField(max_length=254)
    friendly_brand_name = models.CharField(max_length=254)

    def __str__(self):
        return self.friendly_brand_name

    def get_friendly_name(self):
        return self.friendly_brand_name


class BaseProduct(models.Model):

    class Meta:
        abstract = True  # Set this model as Abstract

    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey(ProductBrand, null=True, blank=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    description = tinymce_models.HTMLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {} {}".format(self.brand, self.model, self.name)


class Product(BaseProduct):
    class Meta:
        verbose_name_plural = 'Products'

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)
    special = models.ForeignKey(Special, null=True, blank=True,
                                on_delete=models.SET_NULL)
    brochure = models.URLField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    featured_description = tinymce_models.HTMLField(
        max_length=400,
        default="",
        blank=True,
        verbose_name="Featured description max length 400")

    @property
    def rating(self):
        return self.product_reviews.aggregate(avg_score=Avg('review_score'))[
            'avg_score']
        # https://stackoverflow.com/questions/59479908/how-to-make-an-average-from-values-of-a-foreign-key-in-django


class ProductReviews(models.Model):
    class Meta:
        verbose_name_plural = 'Product Reviews'

    REVIEW_CHOICES = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]

    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL,
                                related_name="product_reviews")
    user = models.ForeignKey(UserProfile, null=True, blank=True,
                             on_delete=models.SET_NULL)
    review_title = models.CharField(max_length=254, null=True, blank=True)
    review_text = models.CharField(max_length=1024, null=True, blank=True)
    review_image = models.ImageField(null=True, blank=True)
    review_score = models.PositiveIntegerField(choices=REVIEW_CHOICES,
                                               validators=[
                                                   MinValueValidator(1),
                                                   MaxValueValidator(5)])
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + "_" + str(self.review_score)


class ProductImages(models.Model):
    class Meta:
        verbose_name_plural = 'Product Images'

    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL,
                                related_name="product_image")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class ProductSpecifications(models.Model):
    """To display extra specifications' product may have(key features)"""

    class Meta:
        verbose_name_plural = 'Product Specifications'

    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE,
                                related_name="product_specifications")
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.CharField(max_length=254, blank=False, null=False)


class Cartridges(BaseProduct):
    """ Cartridges used in printers"""

    class Meta:
        verbose_name_plural = 'Cartridges'

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    compatible_printer = models.ManyToManyField(Product,
                                                related_name='cartridges')
    cartridge_product = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.model
