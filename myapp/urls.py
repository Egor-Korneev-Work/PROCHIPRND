from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:project_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('contacts/', views.contacts, name='contacts'),
]