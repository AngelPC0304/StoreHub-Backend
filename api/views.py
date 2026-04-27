from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Categoria, Producto

# 1. IMPORTAMOS EL NUEVO SERIALIZADOR DEL LOGIN
from .serializers import CategoriaSerializer, ProductoSerializer, RegistroSerializer, CustomTokenObtainPairSerializer 

# 2. IMPORTAMOS LA VISTA BASE DE LOS TOKENS
from rest_framework_simplejwt.views import TokenObtainPairView 

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# --- VISTA PARA REGISTRO ---
class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Permitimos que cualquiera se registre sin token
    serializer_class = RegistroSerializer

# --- NUEVA VISTA PARA EL LOGIN (CON NOMBRE Y APELLIDO) ---
class CustomTokenObtainPairView(TokenObtainPairView):
    # Le decimos a Django que use nuestro serializador personalizado
    serializer_class = CustomTokenObtainPairSerializer