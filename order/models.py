from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import (
    ORDER_CHOICES,
    ORDER_IN_PROGRESS,
)
from .signals import (
    orderitem_pre_save,
    orderitem_post_save,
)


class Order(models.Model):
    """
    Stores information about an order to
    be used as ForeignKey to :model:`order.OrderItem`
    """
    status = models.CharField(
        max_length=32,
        choices=ORDER_CHOICES,
        default=ORDER_IN_PROGRESS,
    )
    customer_name = models.CharField(
        max_length=128,
    )
    customer_address = models.TextField()
    total = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.00'))
        ]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        db_index=True,
        editable=False,
    )

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return "{} - {}".format(self.customer_name, self.total)


class OrderItem(models.Model):
    """
    Stores information about an order item made
    related to :model:`product.Pizza` and
    :model:`product.PizzaSize`
    """
    order = models.ForeignKey(
        'order.Order',
        related_name='items',
        on_delete=models.CASCADE,
    )
    pizza = models.ForeignKey(
        'product.Pizza',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
    )
    size = models.ForeignKey(
        'product.PizzaSize',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
    )
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        db_index=True,
        editable=False,
    )

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __str__(self):
        return "{}".format(self.pizza)


models.signals.pre_save.connect(orderitem_pre_save, sender=OrderItem)
models.signals.post_save.connect(orderitem_post_save, sender=OrderItem)
