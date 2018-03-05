from django.contrib import admin

from .models import (
    Pizza,
    PizzaSize,
)


class PizzaAdmin(admin.ModelAdmin):
    """
    Admin view for :model:`product.Pizza`
    """

    model = Pizza


class PizzaSizeAdmin(admin.ModelAdmin):
    """
    Admin view for :model:`product.PizzaSize`
    """

    model = PizzaSize


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(PizzaSize, PizzaSizeAdmin)
