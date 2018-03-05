# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import (
    Pizza,
    PizzaSize,
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


class PizzaSerializer(serializers.ModelSerializer):
    """
    Serializer to be used by :model:`product.Pizza`
    """

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'sizes',
        )
        read_only_fields = (
            'id',
        )
