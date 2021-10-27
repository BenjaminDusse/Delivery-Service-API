from rest_framework import serializers
from .models import Branch, Status, Order, User


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'phone']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_type']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'name', 'phone', 'address', 'status', 'comment']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone', 'price', 'address', 'comment', 'status']

