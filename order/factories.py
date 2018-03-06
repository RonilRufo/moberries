import factory

from faker import Faker


fake = Faker()


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Order`
    """
    customer_name = fake.name()
    customer_address = fake.address()

    class Meta:
        model = 'order.Order'


class OrderItemFactory(factory.django.DjangoModelFactory):
    """
    Factory for :model:`product.Order`
    """
    order = factory.SubFactory(OrderFactory)

    class Meta:
        model = 'order.OrderItem'
