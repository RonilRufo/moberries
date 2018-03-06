# -*- coding: utf-8 -*-
from rest_framework import serializers

from .fields import (
    CustomerNameField,
    CustomerAddressField,
)
from .models import (
    Order,
    OrderItem,
)
from product.mixins import UpdateSerializerMixin


class OrderSerializer(UpdateSerializerMixin, serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.Order`
    """

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'customer_name',
            'customer_address',
            'total',
            'created_at',
            'last_modified',
        )
        read_only_fields = (
            'id',
            'total',
            'created_at',
            'last_modified',
        )


class OrderItemSerializer(UpdateSerializerMixin, serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.OrderItem`
    """

    customer_name = CustomerNameField(
        max_length=128
    )
    customer_address = CustomerAddressField(
        max_length=255
    )

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'customer_name',
            'customer_address',
            'pizza',
            'size',
            'quantity',
            'price',
            'created_at',
            'last_modified',
        )
        read_only_fields = (
            'id',
            'order',
            'price',
            'created_at',
            'last_modified',
        )
