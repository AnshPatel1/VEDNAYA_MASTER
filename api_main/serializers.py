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
            'type',
            'support_category',
        ]

    extra_kwargs = {}


class ARCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARC
        fields = [
            'pk',
            'name',
            'person_in_charge',
            'business_type',
            'sitting_doctor_id',
            'products_under_support',
        ]

    extra_kwargs = {}


class ChemistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chemist
        fields = [
            'pk',
            'name',
            'person_in_charge',
            'business_type',
            'sitting_doctor_id',
            'products_under_support',
        ]

    extra_kwargs = {}


class MSOSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSO
        fields = [
            'pk',
            'name',
            'hq',
            'territory',
            'connected_doctors',
            'connected_arc',
            'connected_chemists',
        ]

    extra_kwargs = {}

