# orders/utils.py

import string
import secrets
from django.utils.text import slugify

from orders.models import Coupon  # adjust import if your model is elsewhere


def generate_coupon_code(length: int = 10) -> str:
    """
    Generates a unique alphanumeric coupon code.
    Ensures the generated code doesn't already exist in the Coupon table.

    Args:
        length (int): Desired length of the coupon code (default: 10)

    Returns:
        str: A unique coupon code string (e.g., 'A9F2G7K8QJ')
    """

    # Define character pool (uppercase letters + digits)
    characters = string.ascii_uppercase + string.digits

    while True:
        # 1️⃣ Generate random code
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Optional: make it cleaner if you want to show it in UI (like “SAVE-AX12”)
        code = slugify(code).upper().replace('-', '')

        # 2️⃣ Check uniqueness in database
        if not Coupon.objects.filter(code=code).exists():
            return code