# In manage.py shell or data migration:
from orders.models import OrderStatus, PENDING, PROCESSING, COMPLETED, CANCELLED
OrderStatus.objects.get_or_create(name=PENDING)
OrderStatus.objects.get_or_create(name=PROCESSING)
OrderStatus.objects.get_or_create(name=COMPLETED)
OrderStatus.objects.get_or_create(name=CANCELLED)