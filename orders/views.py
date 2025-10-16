from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer

class CouponValidationView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get('code', '').strip()
        today = timezone.now().date()
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                is_active=True,
                valid_from__lte=today,
                valid_until__gte=today
            )
            serializer = CouponSerializer(coupon)
            return Response({"success": True, "discount_percentage": serializer.data['discount_percentage']}, status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            return Response({"success": False, "error": "Invalid or expired coupon code."}, status=status.HTTP_400_BAD_REQUEST)