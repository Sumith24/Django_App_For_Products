from django.urls import path
from core_app import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # add product
    path('add_product/',views.add_product, name='add-product'),

    # product
    path('product/<str:product_id>/',views.view_product, name='view-product'),

    # edit product
    path('edit_product/',views.edit_product, name='edit-product'),

    # delete product
    path('delete_product/<str:product_id>/',views.delete_product, name='delete-product'),
]
