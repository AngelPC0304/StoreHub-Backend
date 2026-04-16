from django.urls import path, include
from rest_framework.routers import DefaultRouter
# ¡Aquí está el cambio! Agregamos RegistroView a la lista de importaciones
from .views import CategoriaViewSet, ProductoViewSet, RegistroView

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('', include(router.urls)),
]