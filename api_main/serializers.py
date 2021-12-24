from rest_framework import serializers
from .models import Product, Doctor, MSO, HQ, ARC, Chemist, SBLR, Stockist, User


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
            'connected_stockists',
        ]

    extra_kwargs = {}


class SBLRSerializer(serializers.ModelSerializer):
    class Meta:
        model = SBLR
        fields = [
            'pk',
            'mso',
            'date',
            'data',
        ]

    extra_kwargs = {}


class StockistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockist
        fields = [
            'pk',
            'name',
            'mobile',
            'gstin',
            'address',
            'person_in_charge',
            'stockist_type',
            'business_type',
        ]

    extra_kwargs = {}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'mso',
            'user',
        ]

    extra_kwargs = {}

