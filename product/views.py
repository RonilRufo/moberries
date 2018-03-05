from rest_framework import viewsets

from .models import (
    Pizza,
    PizzaSize,
)
from .serializers import (
    PizzaSerializer,
    PizzaSizeSerializer,
)


class PizzaSizeViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`sensor.PizzaSize`
    """
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`sensor.Pizza`
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
