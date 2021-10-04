from rest_framework import serializers
from .models import Product, Doctor, MSO, HQ, ARC, Chemist


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'size',
            'type',
        ]

    extra_kwargs = {}


class HQSerializer(serializers.ModelSerializer):
    class Meta:
        model = HQ
        fields = [
            'pk',
            'name',
            'pincode',
        ]

    extra_kwargs = {}


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'pk',
            'name',
            'degree',
            'support_category',
        ]

    extra_kwargs = {}
