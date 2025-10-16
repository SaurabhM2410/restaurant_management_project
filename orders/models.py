from django.db import models

# Assume OrderStatus is already defined above
class Order(models.Model):
    # ... your existing fields ...
    status = models.ForeignKey(
        'OrderStatus',
        on_delete=models.SET_NULL,
        null=True
    )
