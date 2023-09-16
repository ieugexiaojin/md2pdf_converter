# my_django_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('md2pdf/', include('md2pdf_converter.urls')),
]
