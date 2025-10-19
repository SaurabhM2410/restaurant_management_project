# orders/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem  # Assuming OrderItem stores items in each order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']  # Customize based on your OrderItem model


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    date = serializers.DateTimeField(source='created_at', format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'date', 'total_price', 'items']