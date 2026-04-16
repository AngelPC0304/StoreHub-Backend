from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Categoria, Producto

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
        fields = ['username', 'email', 'password', 'first_name', 'rol'] 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        rol_elegido = validated_data.pop('rol')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', '')
        )

        # aqui asigna el rol
        grupo, creado = Group.objects.get_or_create(name=rol_elegido)
        user.groups.add(grupo)

        return user