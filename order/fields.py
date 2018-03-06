from rest_framework import serializers


class CustomerNameField(serializers.CharField):

    def get_attribute(self, obj):
        return obj

    def to_representation(self, obj):
        if hasattr(obj, 'order') and obj.order:
            return obj.order.customer_name
        elif 'customer_name' in obj:
            return obj['customer_name']
        else:
            return ''


class CustomerAddressField(serializers.CharField):

    def get_attribute(self, obj):
        return obj

    def to_representation(self, obj):
        if hasattr(obj, 'order') and obj.order:
            return obj.order.customer_address
        elif 'customer_address' in obj:
            return obj['customer_address']
        else:
            return ''
