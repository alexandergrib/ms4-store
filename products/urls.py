from django.urls import path
from . import views

urlpatterns = [
    # View
    path('', views.all_products, name='products'),
    path('category/', views.all_categories, name='all_categories'),
    path('brand/', views.all_brands, name='all_brands'),
    path('specs/<uuid:product_id>/', views.all_specs, name='all_specs'),
    path('<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('reviews/<uuid:product_id>/', views.all_reviews, name='all_reviews'),
    # Add
    path('add/', views.add_product, name='add_product'),
    path('add/category/', views.add_category, name='add_category'),
    path('add/brand/', views.add_brand, name='add_brand'),
    path('add/specs/<uuid:product_id>', views.add_specs, name='add_specs'),
    path('add/cartridge/<uuid:product_id>', views.add_cartridge,
         name='add_cartridge'),
    path('add/review/<uuid:product_id>/', views.add_review,
         name="add_review"),
    # Edit
    path('edit/product/<uuid:product_id>/', views.edit_product,
         name='edit_product'),
    path('edit/cartridge/<uuid:product_id>/', views.edit_cartridge,
         name='edit_cartridge'),
    path('edit/review/<int:review_id>/', views.edit_review,
         name="edit_review"),
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
    path('delete/cartridge/<uuid:cartridge_id>/', views.delete_cartridge,
         name='delete_cartridge'),
    path('delete/review/<int:review_id>/', views.delete_review,
         name="delete_review"),
]
