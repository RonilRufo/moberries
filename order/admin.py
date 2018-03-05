from django.contrib import admin

from .models import (
    Order,
    OrderItem,
)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin view for :model:`product.Order`
    """

    model = Order


class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin view for :model:`product.OrderItem`
    """

    model = OrderItem


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
