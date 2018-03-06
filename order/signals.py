from django.apps import apps
from django.db.models import Sum


def orderitem_pre_save(sender, instance, **kwargs):
    """
    Function to be used as signal (pre_save) when saving
    :model:`order.OrderItem`

    Function(s) to be executed:
        - calculates the value for `price` of the
          :model:`order.OrderItem` object using the `quantity`
          and the `price` of the :model:`product.PizzaVariation`
    """
    PizzaVariation = apps.get_model('product', 'PizzaVariation')
    variation = PizzaVariation.objects.get(
        pizza=instance.pizza,
        size=instance.size,
    )
    instance.price = instance.quantity * variation.price


def orderitem_post_save(sender, instance, created, **kwargs):
    """
    Function to be used as signal (post_save) when saving
    :model:`order.OrderItem`

    Function(s) to be executed:
        - calculates total price of the :model:`order.Order`
          object represented by the `total` field
    """
    order = instance.order
    amount = order.items.aggregate(Sum('price'))
    if amount and amount['price__sum']:
        order.total = amount['price__sum']
        order.save()
