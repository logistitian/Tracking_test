from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('delivery-request/', views.delivery_request, name='delivery_request'),
]