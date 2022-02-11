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


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SampleSerializer


class SampleList(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SampleSerializer


class POPList(generics.ListCreateAPIView):
    queryset = POP.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = POPSerializer


class POPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = POP.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = POPSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

    @api_view(['GET', ])
    def get_id_by_name(request):
        name = request.query_params['name']
        try:
            product = Product.objects.get(name=name)
            product_data = ProductSerializer(product)
            id = product_data.data['pk']
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"id": id})


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


@api_view(['GET', ])
def get_stockists_by_doctor_id(request):
    id = request.query_params['id']
    try:
        doctor = Doctor.objects.get(id=id)
        doctor_data = DoctorSerializer(doctor)
        connected_stockists = doctor_data.data['connected_stockists']
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return_data = []
        for stockist in connected_stockists:
            stockist = Stockist.objects.get(id=stockist)
            serializer = StockistSerializer(stockist)
            return_data.append(serializer.data)
        return Response(return_data)


class ARCList(generics.ListCreateAPIView):
    queryset = ARC.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ARCSerializer


@api_view(['GET', ])
def get_stockists_by_arc_id(request):
    id = request.query_params['id']
    try:
        arc = ARC.objects.get(id=id)
        arc_data = ARCSerializer(arc)
        connected_stockists = arc_data.data['connected_stockists']
    except Chemist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return_data = []
        for stockist in connected_stockists:
            stockist = Stockist.objects.get(id=stockist)
            serializer = StockistSerializer(stockist)
            return_data.append(serializer.data)
        return Response(return_data)


class ARCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ARC.objects.all()
    permission_classes = []
    serializer_class = ARCSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer


class ChemistList(generics.ListCreateAPIView):
    queryset = Chemist.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ChemistSerializer


@api_view(['GET', ])
def get_stockists_by_chemist_id(request):
    id = request.query_params['id']
    try:
        chemist = Chemist.objects.get(id=id)
        chemist_data = ChemistSerializer(chemist)
        connected_stockists = chemist_data.data['connected_stockists']
    except Chemist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return_data = []
        for stockist in connected_stockists:
            stockist = Stockist.objects.get(id=stockist)
            serializer = StockistSerializer(stockist)
            return_data.append(serializer.data)
        return Response(return_data)


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
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_stockists(request, id):
        try:
            mso = MSO.objects.get(id=id)
            mso_data = MSOSerializer(mso)
            connected_stockists = mso_data.data['connected_stockists']
        except MSO.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for stockist in connected_stockists:
                stockist = Stockist.objects.get(id=stockist)
                serializer = StockistSerializer(stockist)
                return_data.append(serializer.data)
            return Response({id: return_data})


class MSODetailQs(generics.RetrieveUpdateDestroyAPIView):
    queryset = MSO.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MSOSerializer

    @api_view(['GET', ])
    def connected_doctors(request):
        id = request.query_params['id']
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
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_arcs(request):
        id = request.query_params['id']
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
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_chemists(request):
        id = request.query_params['id']
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
            return Response({id: return_data})

    @api_view(['GET', ])
    def connected_stockists(request):
        id = request.query_params['id']
        try:
            mso = MSO.objects.get(id=id)
            mso_data = MSOSerializer(mso)
            connected_stockists = mso_data.data['connected_stockists']
        except MSO.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return_data = []
            for stockist in connected_stockists:
                stockist = Stockist.objects.get(id=stockist)
                serializer = StockistSerializer(stockist)
                return_data.append(serializer.data)
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


class UserList(generics.ListCreateAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = SBLRSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SBLR.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = SBLRSerializer


@api_view(['GET', ])
def get_mso_by_user(request):
    username = request.query_params['username']
    password = request.query_params['passwd']
    try:
        user = authenticate(username=username, password=password)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if user is None:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if user.is_authenticated:
            _id = user.id
            user = User.objects.get(user=_id)
            user_serialized = UserSerializer(user)
            user = user_serialized.data
            mso_id = int(user['mso'])
            mso = MSO.objects.get(id=mso_id)
            serializer = MSOSerializer(mso)
            return Response(serializer.data, 200)


@api_view(['GET', ])
def list_recent_sblrs_by_mso(request):
    mso_id = int(request.query_params['id'])
    try:
        sblrs = SBLR.objects.filter(mso=mso_id)
    except SBLR.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return_data = []
        for sblr in sblrs:
            serializer = SBLRSerializer(sblr)
            return_data.append(serializer.data)
        return_data.reverse()
        return Response(return_data)
