# orders/views.py

from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer


class UserOrderHistoryView(generics.ListAPIView):
    """
    GET /api/orders/history/
    Returns a list of past orders for the authenticated user.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return orders only for the logged-in user, most recent first
        return Order.objects.filter(user=self.request.user).order_by('-created_at')