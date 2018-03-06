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
    ---
    create:
        Creates :model:`product.PizzaSize` object
    update:
        Updates :model:`product.PizzaSize` object

    retrieve:
        Retrieves a :model:`product.PizzaSize` instance

    list:
        Returns list of all :model:`product.PizzaSize`

    delete:
        Removes/Deletes :model:`product.PizzaSize` objects

    """
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.Pizza`
    ---
    create:
        Creates :model:`product.Pizza` object
    update:
        Updates :model:`product.Pizza` object

    retrieve:
        Retrieves a :model:`product.Pizza` instance

    list:
        Returns list of all :model:`product.Pizza`

    delete:
        Removes/Deletes :model:`product.Pizza` objects

    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaVariationViewSet(viewsets.ModelViewSet):
    """
    CRUD for :model:`product.PizzaVariation`
    ---
    create:
        Creates :model:`product.PizzaVariation` object
    update:
        Updates :model:`product.PizzaVariation` object

    retrieve:
        Retrieves a :model:`product.PizzaVariation` instance

    list:
        Returns list of all :model:`product.PizzaVariation`

    delete:
        Removes/Deletes :model:`product.PizzaVariation` objects

    """
    queryset = PizzaVariation.objects.all()
    serializer_class = PizzaVariationSerializer
