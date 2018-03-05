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

    @factory.post_generation
    def sizes(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for size in extracted:
                self.sizes.add(size)
