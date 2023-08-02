from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/add/', views.add_product, name='add_product'),
    path('<int:category_id>/update/<int:product_id>/', views.update_product, name='update_product'),
    path('<int:category_id>/remove/<int:product_id>/', views.remove_product, name='remove_product'),
    path('categories/<int:category_id>/products/', views.product_list, name='product_list'),
]