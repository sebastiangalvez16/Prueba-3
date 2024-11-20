from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, cliente_list, cliente_create, cliente_update, cliente_delete

# Configuración del router para la API
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),

    # Rutas para templates
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/create/', cliente_create, name='cliente_create'),
    path('clientes/update/<int:pk>/', cliente_update, name='cliente_update'),
    path('clientes/delete/<int:pk>/', cliente_delete, name='cliente_delete'),
]
