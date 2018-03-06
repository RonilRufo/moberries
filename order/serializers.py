# -*- coding: utf-8 -*-
from rest_framework import serializers

from product.mixins import UpdateSerializerMixin
from .models import (
    Order,
    OrderItem,
)


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

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'pizza',
            'size',
            'quantity',
            'price',
            'created_at',
            'last_modified',
        )
        read_only_fields = (
            'id',
            'price',
            'created_at',
            'last_modified',
        )
