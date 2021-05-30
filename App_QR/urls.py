from django.urls import path 
from . import views

app_name = "App_QR"

urlpatterns = [
    path('', views.upload_qr, name='upload'),
    path('success/', views.success, name='success'),
]
