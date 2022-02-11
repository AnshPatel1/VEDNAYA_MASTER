from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('products/get_id_by_name', views.ProductDetail.get_id_by_name),
    path('samples', views.SampleList.as_view()),
    path('pops', views.POPList.as_view()),
    path('pops/<int:pk>', views.POPDetail.as_view()),
    path('samples/<int:pk>', views.SampleDetail.as_view()),
    path('hqs', views.HQList.as_view()),
    path('hqs/<int:pk>', views.HQDetail.as_view()),
    path('hqs/mso/<int:hq>', views.HQDetail.get_mso),
    path('doctors', views.DoctorList.as_view()),
    path('doctors/<int:pk>', views.DoctorDetail.as_view()),
    path('doctors/connected_stockists', views.get_stockists_by_doctor_id),
    path('arcs', views.ARCList.as_view()),
    path('arcs/<int:pk>', views.ARCDetail.as_view()),
    path('arcs/connected_stockists', views.get_stockists_by_arc_id),
    path('chemists', views.ChemistList.as_view()),
    path('chemists/<int:pk>', views.ChemistDetail.as_view()),
    path('chemists/connected_stockists', views.get_stockists_by_chemist_id),
    path('msos', views.MSOList.as_view()),
    path('msos/<int:pk>', views.MSODetail.as_view()),
    path('msos/<int:id>/doctors', views.MSODetail.connected_doctors),
    path('msos/doctors', views.MSODetailQs.connected_doctors),
    path('msos/<int:id>/arcs', views.MSODetail.connected_arcs),
    path('msos/arcs', views.MSODetailQs.connected_arcs),
    path('msos/<int:id>/chemists', views.MSODetail.connected_chemists),
    path('msos/chemists', views.MSODetailQs.connected_chemists),
    path('msos/<int:id>/stockists', views.MSODetail.connected_stockists),
    path('msos/stockists', views.MSODetailQs.connected_stockists),
    path('sblrs', views.SBLRList.as_view()),
    path('sblrs/id/<int:pk>', views.SBLRDetail.as_view()),
    path('sblrs/<int:mso_id>', views.SBLRDetail.list_sblrs_by_mso),
    path('sblrs/recent', views.list_recent_sblrs_by_mso),
    path('sblrs/<str:date>', views.SBLRDetail.list_sblrs_by_date),
    path('app/login', views.get_mso_by_user),










    ######################################

    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('products/get_id_by_name/', views.ProductDetail.get_id_by_name),
    path('samples/', views.SampleList.as_view()),
    path('pops/', views.POPList.as_view()),
    path('pops/<int:pk>/', views.POPDetail.as_view()),
    path('samples/<int:pk>/', views.SampleDetail.as_view()),
    path('hqs/', views.HQList.as_view()),
    path('hqs/<int:pk>/', views.HQDetail.as_view()),
    path('hqs/mso/<int:hq>/', views.HQDetail.get_mso),
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
    path('doctors/connected_stockists/', views.get_stockists_by_doctor_id),
    path('arcs/', views.ARCList.as_view()),
    path('arcs/<int:pk>/', views.ARCDetail.as_view()),
    path('arcs/connected_stockists/', views.get_stockists_by_arc_id),
    path('chemists/', views.ChemistList.as_view()),
    path('chemists/<int:pk>/', views.ChemistDetail.as_view()),
    path('chemists/connected_stockists/', views.get_stockists_by_chemist_id),
    path('msos/', views.MSOList.as_view()),
    path('msos/<int:pk>/', views.MSODetail.as_view()),
    path('msos/<int:id>/doctors/', views.MSODetail.connected_doctors),
    path('msos/doctors/', views.MSODetailQs.connected_doctors),
    path('msos/<int:id>/arcs/', views.MSODetail.connected_arcs),
    path('msos/arcs/', views.MSODetailQs.connected_arcs),
    path('msos/<int:id>/chemists/', views.MSODetail.connected_chemists),
    path('msos/chemists/', views.MSODetailQs.connected_chemists),
    path('msos/<int:id>/stockists/', views.MSODetail.connected_stockists),
    path('msos/stockists/', views.MSODetailQs.connected_stockists),
    path('sblrs/', views.SBLRList.as_view()),
    path('sblrs/id/<int:pk>/', views.SBLRDetail.as_view()),
    path('sblrs/<int:mso_id>/', views.SBLRDetail.list_sblrs_by_mso),
    path('sblrs/recent/', views.list_recent_sblrs_by_mso),
    path('sblrs/<str:date>/', views.SBLRDetail.list_sblrs_by_date),
    path('app/login/', views.get_mso_by_user),

]
