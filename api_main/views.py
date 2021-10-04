import simplejson
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


class SBLRList(generics.ListCreateAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SBLRSerializer


class SBLRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SBLRSerializer


@api_view(['GET', ])
def list_sblrs(request, mso_id):
    try:
        sblrs = SBLR.objects.filter(mso=mso_id)
    except SBLR.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return_data = []
        for sblr in sblrs:
            serializer = SBLRSerializer(sblr)
            return_data.append(serializer.data)
        return Response({mso_id: return_data})



