from django.urls import path
from . import views

urlpatterns = [
    # View
    path('', views.all_products, name='products'),
    path('<uuid:product_id>/', views.product_detail, name='product_detail'),
    # Add
    path('add/', views.add_product, name='add_product'),
    path('add/category/', views.add_category, name='add_category'),
    path('add/brand/', views.add_brand, name='add_brand'),
    # Edit
    path('edit/<uuid:product_id>/', views.edit_product, name='edit_product'),
    # Delete
    path('delete/<uuid:product_id>/', views.delete_product,
         name='delete_product'),
]
