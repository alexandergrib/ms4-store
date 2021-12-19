from django.urls import path
from . import views

urlpatterns = [
    # View
    path('', views.all_products, name='products'),
    path('category/', views.all_categories, name='all_categories'),
    path('brand/', views.all_brands, name='all_brands'),
    path('specs/<uuid:product_id>/', views.all_specs, name='all_specs'),
    path('<uuid:product_id>/', views.product_detail, name='product_detail'),
    # Add
    path('add/', views.add_product, name='add_product'),
    path('add/category/', views.add_category, name='add_category'),
    path('add/brand/', views.add_brand, name='add_brand'),
    path('add/specs/<uuid:product_id>', views.add_specs, name='add_specs'),
    # Edit
    path('edit/<uuid:product_id>/', views.edit_product, name='edit_product'),
    # Delete
    path('delete/<uuid:product_id>/', views.delete_product,
         name='delete_product'),
    path('delete/brand/<brand_id>/', views.delete_brand,
         name='delete_brand'),
    path('delete/category/<category_id>/', views.delete_category,
         name='delete_category'),
    path('delete/image/<image_id>/', views.delete_image,
         name='delete_image'),
    path('delete/spec/<spec_id>/', views.delete_spec,
         name='delete_spec'),
]
