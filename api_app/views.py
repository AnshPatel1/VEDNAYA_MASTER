from rest_framework import generics, permissions
from .models import *
from .serializers import *


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer


class HQList(generics.ListCreateAPIView):
    queryset = HQ.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HQSerializer


class HQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HQ.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HQSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DoctorSerializer


class ARCList(generics.ListCreateAPIView):
    queryset = ARC.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ARCSerializer


class ARCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ARC.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ARCSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer


class ChemistList(generics.ListCreateAPIView):
    queryset = Chemist.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ChemistSerializer


class ChemistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chemist.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChemistSerializer


class MSOList(generics.ListCreateAPIView):
    queryset = MSO.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MSOSerializer


class MSODetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MSO.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MSOSerializer
