# -*- coding: utf-8 -*-
from rest_framework import serializers

from .mixins import UpdateSerializerMixin
from .models import (
    Pizza,
    PizzaSize,
    PizzaVariation,
)


class PizzaSizeSerializer(serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.PizzaSize`
    """

    class Meta:
        model = PizzaSize
        fields = (
            'id',
            'size',
        )
        read_only_fields = (
            'id',
        )


class PizzaSerializer(UpdateSerializerMixin, serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.Pizza`
    """

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )


class PizzaVariationSerializer(UpdateSerializerMixin, serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.PizzaVariation`
    """

    class Meta:
        model = PizzaVariation
        fields = (
            'id',
            'pizza',
            'size',
            'price',
        )
        read_only_fields = (
            'id',
        )
