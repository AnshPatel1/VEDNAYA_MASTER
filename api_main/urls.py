from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('hqs', views.HQList.as_view()),
    path('hqs/<int:pk>', views.HQDetail.as_view()),
    path('doctors', views.DoctorList.as_view()),
    path('doctors/<int:pk>', views.DoctorDetail.as_view()),
    path('arcs', views.ARCList.as_view()),
    path('arcs/<int:pk>', views.ARCDetail.as_view()),
    path('chemists', views.ChemistList.as_view()),
    path('chemists/<int:pk>', views.ChemistDetail.as_view()),
    path('msos', views.MSOList.as_view()),
    path('msos/<int:pk>', views.MSODetail.as_view()),
    path('sblrs', views.SBLRList.as_view()),
    path('sblrs/id/<int:pk>', views.SBLRDetail.as_view()),
    path('sblrs/<int:mso_id>', views.SBLRDetail.list_sblrs_by_mso, name="detail"),
    path('sblrs/<str:date>', views.SBLRDetail.list_sblrs_by_date, name="sblr_date"),
]
