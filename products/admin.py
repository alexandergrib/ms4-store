from django.contrib import admin
from .models import Product, Category, ProductImages, ProductReviews

list_display = (
    'sku',
    'name',
    'category',
    'price',
    'product_rating',
    'specifications',
    'created_at',
    'created_by',
    'modified_by'
)


class ProductAdmin(admin.ModelAdmin):

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'image_url',
        'image',
    )


class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'review_text',
        'review_image',
        'review_score',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
