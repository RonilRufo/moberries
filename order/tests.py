from django.urls import reverse

from decimal import Decimal
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import (
    OrderItemFactory,
)
from product.factories import (
    HawaiianPizzaFactory,
    PizzaSize50Factory,
    PizzaVariationFactory,
)


fake = Faker()


class TestOrderItem(APITestCase):
    """
    Test cases for :model:`order.OrderItem`
    """
    def setUp(self):
        pizza = HawaiianPizzaFactory()
        size = PizzaSize50Factory()
        # Make sure to create a Variation first
        # before creating an order item
        self.variation = PizzaVariationFactory(
            pizza=pizza,
            size=size,
            price=Decimal('8.99')
        )
        self.item = OrderItemFactory(
            pizza=self.variation.pizza,
            size=self.variation.size,
            quantity=2
        )
        # order = OrderFactory()
        self.payload = {
            # 'order': order.pk,
            'customer_name': fake.name(),
            'customer_address': fake.address(),
            'pizza': pizza.pk,
            'size': size.pk,
            'quantity': 3
        }
        self.url = reverse('orderitem-list')
        self.detail_url = reverse(
            'orderitem-detail',
            kwargs={'pk': self.item.pk}
        )

    def test_get_order_item_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order_item_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order_item(self):
        response = self.client.post(self.url, self.payload)
        subtotal = self.variation.price * self.payload.get('quantity')
        self.assertEqual(subtotal, Decimal(response.data['price']))

    def test_update_order_item(self):
        quantity = 1
        payload = {
            "quantity": quantity
        }
        subtotal = self.variation.price * quantity
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(subtotal, Decimal(response.data['price']))

    def test_delete_order_item(self):
        response = self.client.delete(self.detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
