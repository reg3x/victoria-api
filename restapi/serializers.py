from rest_framework import serializers
from models import Panty, Legging, Brasier, Cream, Butter, Fragance


class PantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Panty
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class LeggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legging
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class BrasierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brasier
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class CreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cream
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class ButterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Butter
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class FraganceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fragance
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')
