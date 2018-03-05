import factory


class PizzaSizeFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.PizzaSize`
    """

    class Meta:
        model = 'product.PizzaSize'
        django_get_or_create = ('size', )


class HawaiianPizzaFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Pizza` with `Hawaiian`
    as value for `name`
    """
    name = "Hawaiian"

    class Meta:
        model = 'product.Pizza'
        django_get_or_create = ('name', )
