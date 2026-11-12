from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('product/', views.index),
    path('product/time', views.rezero),
    path('product/<int:id>/', views.product),
    path('product/<int:id>/buy/', views.buy),
]
