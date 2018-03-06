import factory

from decimal import Decimal


class PizzaSizeFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaSize`
    """

    class Meta:
        model = 'product.PizzaSize'
        django_get_or_create = ('size', )


class PizzaSize30Factory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaSize` with `30`
    as value for `size`
    """
    size = 30

    class Meta:
        model = 'product.PizzaSize'
        django_get_or_create = ('size', )


class PizzaSize50Factory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaSize` with `50`
    as value for `size`
    """
    size = 50

    class Meta:
        model = 'product.PizzaSize'
        django_get_or_create = ('size', )


class PizzaFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Pizza` with `Hawaiian`
    as value for `name`
    """

    class Meta:
        model = 'product.Pizza'
        django_get_or_create = ('name', )


class HawaiianPizzaFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Pizza` with `Hawaiian`
    as value for `name`
    """
    name = "Hawaiian"

    class Meta:
        model = 'product.Pizza'
        django_get_or_create = ('name', )


class HawaiianSize30Factory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaVariation` with `Hawaiian`
    as value for :model:`product.Pizza` and `30` as value
    for :model:`product.PizzaSize`
    """
    pizza = factory.SubFactory(HawaiianPizzaFactory)
    size = factory.SubFactory(PizzaSize30Factory)
    price = Decimal('10')

    class Meta:
        model = 'product.PizzaVariation'
        django_get_or_create = ('pizza', 'size')


class HawaiianSize50Factory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaVariation` with `Hawaiian`
    as value for :model:`product.Pizza` and `50` as value
    for :model:`product.PizzaSize`
    """
    pizza = factory.SubFactory(HawaiianPizzaFactory)
    size = factory.SubFactory(PizzaSize50Factory)
    price = Decimal('12')

    class Meta:
        model = 'product.PizzaVariation'
        django_get_or_create = ('pizza', 'size')


class PizzaVariationFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaVariation`
    """

    class Meta:
        model = 'product.PizzaVariation'
        django_get_or_create = ('pizza', 'size')
