import factory

from decimal import Decimal
from faker import Faker

from product.factories import (
    HawaiianPizzaFactory,
    PizzaSize30Factory,
)


fake = Faker()


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Order`
    """
    customer_name = fake.name()
    customer_address = fake.address()
    total = Decimal('0.00')

    class Meta:
        model = 'order.Order'


class OrderItemFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Order`
    """
    order = factory.SubFactory(OrderFactory)

    class Meta:
        model = 'order.OrderItem'
