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

    @api_view(['GET', ])
    def get_mso(request, hq):
        try:
            msos = MSO.objects.filter(hq=hq)
        except HQ.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for mso in msos:
                serializer = MSOSerializer(mso)
                return_data.append(serializer.data)
            return Response({hq: return_data})


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

    @api_view(['GET', ])
    def connected_doctors(request, id):
        try:
            mso = MSO.objects.get(id=id)
            mso_data = MSOSerializer(mso)
            connected_doctors = mso_data.data['connected_doctors']
        except MSO.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for doctor in connected_doctors:
                doctor = Doctor.objects.get(id=doctor)
                serializer = DoctorSerializer(doctor)
                return_data.append(serializer.data)
                print(serializer.data)
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_arcs(request, id):
        try:
            mso = MSO.objects.get(id=id)
            mso_data = MSOSerializer(mso)
            connected_arcs = mso_data.data['connected_arc']
        except MSO.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for arc in connected_arcs:
                arc = ARC.objects.get(id=arc)
                serializer = ARCSerializer(arc)
                return_data.append(serializer.data)
                print(serializer.data)
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_chemists(request, id):
        try:
            mso = MSO.objects.get(id=id)
            mso_data = MSOSerializer(mso)
            connected_chemists = mso_data.data['connected_chemists']
        except MSO.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for chemist in connected_chemists:
                chemist = Chemist.objects.get(id=chemist)
                serializer = ChemistSerializer(chemist)
                return_data.append(serializer.data)
                print(serializer.data)
            return Response({id: return_data})


class SBLRList(generics.ListCreateAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SBLRSerializer


class SBLRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SBLRSerializer

    @api_view(['GET', ])
    def list_sblrs_by_mso(request, mso_id):
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

    @api_view(['GET', ])
    def list_sblrs_by_date(request, date):
        try:
            sblrs = SBLR.objects.filter(date=date)
        except SBLR.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for sblr in sblrs:
                serializer = SBLRSerializer(sblr)
                return_data.append(serializer.data)
            return Response({date: return_data})



