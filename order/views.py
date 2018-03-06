from rest_framework import viewsets

from .models import (
    Order,
    OrderItem,
)
from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.Order`
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.OrderItem`
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
