"""moberries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from order.views import (
    OrderViewSet,
    OrderItemViewSet,
)
from product.views import (
    PizzaViewSet,
    PizzaSizeViewSet,
    PizzaVariationViewSet,
)


schema_view = get_swagger_view(title='MoBerries API')

router = DefaultRouter()
router.register(r'pizza-sizes', PizzaSizeViewSet)
router.register(r'pizzas', PizzaViewSet)
router.register(r'pizza-variations', PizzaVariationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'api-auth/', include('rest_framework.urls')),
    path(r'api/v1/', include(router.urls)),
    path(r'docs/', schema_view),
]
