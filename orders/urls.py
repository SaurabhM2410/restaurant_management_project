# orders/urls.py

from django.urls import path
from .views import UserOrderHistoryView

urlpatterns = [
    path('orders/history/', UserOrderHistoryView.as_view(), name='order-history'),
]