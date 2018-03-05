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
    Stores basic information about a Pizza.
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


class PizzaVariation(models.Model):
    """
    Stores available variations for each
    :model:`product.Pizza`. Variations are represented
    by :model:`product.PizzaSize`
    """
    pizza = models.ForeignKey(
        'product.Pizza',
        related_name='variations',
        on_delete=models.CASCADE,
    )
    size = models.ForeignKey(
        'product.PizzaSize',
        related_name='pizza_variations',
        on_delete=models.SET_NULL,
        null=True,
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    class Meta:
        verbose_name = _('Pizza Variation')
        verbose_name_plural = _('Pizza Variations')
        unique_together = ('pizza', 'size')
