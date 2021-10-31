from django.urls import path
from django.views.generic.base import View
from . import views


urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),
    path('product-list/',views.showAll, name='product-list'),
    path('product-detail/<int:pk>',views.viewProduct, name='product-detail'),
    path('product-create/',views.createProduct, name='product-create'),
    path('product-update/<int:pk>',views.updateProduct, name='product-update'),
    ]