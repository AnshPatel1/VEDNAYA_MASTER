"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('api/', include('api_main.urls'), name="api_main"),
    path('admin/database/login/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name="docs"),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name="docs"),
    # path('/', SpectacularSwaggerView.as_view(url_name='schema'), name="docs"),
    # path("", include("dashboard.authentication.urls")),  # Auth routes - login / register
    # path("", include("dashboard.app.urls"))
]

admin.site.site_header = "Vedanya healthcare admin"
admin.site.site_title = "Vedanya healthcare admin site"
admin.site.index_title = "Vedanya Healthcare Admin"
