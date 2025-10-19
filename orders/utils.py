# orders/utils.py

from datetime import date as dt_date
from decimal import Decimal
from django.db.models import Sum
from .models import Order  # Import your Order model


def get_daily_sales_total(date: dt_date) -> Decimal:
    """
    Calculate total sales for a given date by summing total_price of all orders.

    Args:
        date (datetime.date): The specific date to calculate sales for.

    Returns:
        Decimal: Total sales amount for the day. Returns 0 if no orders.
    """

    # Filter orders for the given date
    orders = Order.objects.filter(created_at__date=date)

    # Aggregate sum of total_price
    total_sum = orders.aggregate(total_sum=Sum('total_price'))['total_sum']

    # Return total or 0 if no orders
    return total_sum if total_sum else Decimal('0.00')