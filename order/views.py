from rest_framework import viewsets, mixins

from .constants import ORDER_IN_PROGRESS
from .models import (
    Order,
    OrderItem,
)
from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
)


class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    ViewSet that handles :model:`product.Order` requests.
    This is missing the `CREATE` mixin because we don't
    allow creation of orders. Creation of orders are done
    automatically via creation of :model:`order.OrderItem`
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.OrderItem`
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        customer_name = serializer.validated_data.pop('customer_name')
        customer_address = serializer.validated_data.pop('customer_address')
        order, created = Order.objects.get_or_create(
            customer_name=customer_name,
            status=ORDER_IN_PROGRESS,
            defaults={
                'customer_address': customer_address
            }
        )
        serializer.save(order=order)
