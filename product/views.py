from rest_framework import viewsets

from .models import (
    Pizza,
    PizzaSize,
    PizzaVariation,
)
from .serializers import (
    PizzaSerializer,
    PizzaSizeSerializer,
    PizzaVariationSerializer,
)


class PizzaSizeViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.PizzaSize`
    """
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.Pizza`
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaVariationViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.PizzaVariation`
    """
    queryset = PizzaVariation.objects.all()
    serializer_class = PizzaVariationSerializer
