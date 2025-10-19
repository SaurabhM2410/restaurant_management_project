# menu/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django.db.models import Q

from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemSearchPagination(PageNumberPagination):
    page_size = 10  # default items per page
    page_size_query_param = 'page_size'
    max_page_size = 50


class MenuItemSearchViewSet(viewsets.ViewSet):
    """
    GET /api/menu/search/?q=<query>
    Returns menu items that match or partially match the search query.
    """

    permission_classes = [AllowAny]  # Public endpoint
    pagination_class = MenuItemSearchPagination

    def list(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return Response(
                {"error": "Search query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Case-insensitive partial match
        menu_items = MenuItem.objects.filter(name__icontains=query).order_by('name')

        # Pagination
        paginator = self.pagination_class()
        paginated_items = paginator.paginate_queryset(menu_items, request)
        serializer = MenuItemSerializer(paginated_items, many=True)

        return paginator.get_paginated_response(serializer.data)