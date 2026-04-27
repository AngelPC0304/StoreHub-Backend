from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Categoria, Producto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # <- 1. NUEVA IMPORTACIÓN

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # 2. Agregamos 'last_name' a la lista de campos permitidos
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'rol'] 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        rol_elegido = validated_data.pop('rol')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '') # <- 3. LO GUARDAMOS EN LA BASE DE DATOS
        )

        # aqui asigna el rol
        grupo, creado = Group.objects.get_or_create(name=rol_elegido)
        user.groups.add(grupo)

        return user

# 4. Ahora si les tiene que mostrar el nombre
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        
        data = super().validate(attrs)
        
        data['nombre'] = self.user.first_name
        data['apellidos'] = self.user.last_name
        
        return data