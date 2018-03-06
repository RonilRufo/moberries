# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

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

    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'customer_name',
            'customer_address',
            'total',
            'items',
            'created_at',
            'last_modified',
        )
        read_only_fields = (
            'id',
            'total',
            'items',
            'created_at',
            'last_modified',
        )

    def get_items(self, obj):
        serializer = OrderItemSerializer(obj.items.all(), many=True)
        return serializer.data


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

    def validate(self, data):
        if self.instance and self.instance.pk is not None and \
           not self.instance.order.is_in_progress:
            raise serializers.ValidationError(
                _("Order was either paid, completed, or cancelled already.")
            )
        return data
