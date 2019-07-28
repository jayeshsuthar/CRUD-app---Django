from django.urls import path

from .views import product_list, ProductView, ProductUpdate, ProductDelete, ProductCreate

urlpatterns = [
    path('', product_list.as_view(), name='product_list'),
    path('view/<int:pk>', ProductView.as_view(), name='product_view'),
    path('new', ProductCreate.as_view(), name='product_create'),
    path('view/<int:pk>', ProductView.as_view(), name='product_view'),
    path('edit/<int:pk>', ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
]