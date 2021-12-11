from django.contrib import admin
from .models import (Product, Category,
                     ProductImages, ProductReviews,
                     ProductSpecifications, ProductBrand,
                     Cartridges)

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


class ImagesAdminInline(admin.TabularInline):
    model = ProductImages


class SpecsAdminInline(admin.TabularInline):
    model = ProductSpecifications


class CartridgesAdminInline(admin.TabularInline):
    verbose_name = "Cartridges"
    verbose_name_plural = "Cartridges"
    model = Cartridges.compatible_printer.through


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImagesAdminInline, SpecsAdminInline, CartridgesAdminInline)
    ordering = ('-id',)


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


class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = 'brand_name',


class CartridgesAdmin(admin.ModelAdmin):
    ordering = ('brand',)







admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
# admin.site.register(ProductSpecifications, ProductSpecificationsAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(Cartridges, CartridgesAdmin)
