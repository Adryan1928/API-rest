from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('clientes/', include('cliente.urls'))
]
