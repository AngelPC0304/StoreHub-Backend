from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, RegistroSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# --- NUEVA VISTA PARA REGISTRO ---
class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Permitimos que cualquiera se registre sin token
    serializer_class = RegistroSerializer