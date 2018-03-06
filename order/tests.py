from django.urls import reverse

from decimal import Decimal
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from .constants import (
    ORDER_PAID,
    ORDER_COMPLETED,
)
from .factories import (
    OrderItemFactory,
)
from product.factories import (
    HawaiianPizzaFactory,
    PizzaSize50Factory,
    PizzaVariationFactory,
)


fake = Faker()


class TestOrder(APITestCase):
    """
    Test cases for :model:`order.Order`
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
        self.order = self.item.order
        self.url = reverse('order-list')
        self.detail_url = reverse(
            'order-detail',
            kwargs={'pk': self.order.pk}
        )

    def test_get_order_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        payload = {
            "status": ORDER_PAID
        }
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(self.detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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
        self.payload = {
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

    def test_update_order_item_completed(self):
        quantity = 1
        payload = {
            "quantity": quantity
        }

        order = self.item.order
        order_url = reverse(
            'order-detail',
            kwargs={'pk': order.pk}
        )
        order_payload = {
            'status': ORDER_COMPLETED
        }
        self.client.put(order_url, order_payload)
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
