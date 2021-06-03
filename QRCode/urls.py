from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from App_QR import views


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('qr/', views.upload_qr, name="upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


