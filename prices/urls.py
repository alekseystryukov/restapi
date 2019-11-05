from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prices/', views.PricesListView.as_view(), name='prices-list'),
    path('prices/<int:pk>/', views.PriceDetailView.as_view(), name='prices-detail'),
    path('md-prices/', views.MDPricesListView.as_view(), name='md-prices-list'),
    path('md-prices/<str:pk>/', views.MDPriceDetailView.as_view(), name='md-prices-detail'),
]
