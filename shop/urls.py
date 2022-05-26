from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductView.as_view(), name='landing_page'),
    path('<slug:slug>/', views.Product_DetailView.as_view(),name='product_detail'),
]