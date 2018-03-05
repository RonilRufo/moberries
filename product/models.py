from django.db import models
from django.utils.translation import ugettext_lazy as _


class PizzaSize(models.Model):
    """
    Stores information about pizza sizes
    """
    size = models.PositiveSmallIntegerField(
        unique=True,
        help_text=_('in centimeter(cm)'),
    )

    class Meta:
        verbose_name = _('Pizza Size')
        verbose_name_plural = _('Pizza Sizes')
        ordering = ['size']

    def __str__(self):
        return "{} cm".format(self.size)


class Pizza(models.Model):
    """
    Stores information about a Pizza. Also stores
    a list of :model:`product.PizzaSize` available
    to a certain pizza.
    """
    name = models.CharField(
        max_length=64,
        unique=True,
    )

    class Meta:
        verbose_name = _('Pizza')
        verbose_name_plural = _('Pizzas')

    def __str__(self):
        return "{}".format(self.name)
