from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

#FORMULARIO REGISTROS CITAS
class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields= "__all__"

# FORMULATIO REGISTRO PORTAFOLIO
class PortafolioTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= Portafolio_Tatuadores
        fields=(
            'tatuador',
            'imagen',
            'descripcion'
        )


# FORMULARIOS  REGISTROS USUARIOS

class RegistroUsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroUsuarios
        fields= (
            'nombre',
            'apellido',
            'telefono',
            'contraseña',
            'email'
        )
# FORMULARIOS REGISTROS TATUADORES
class RegistroTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroTatuadores
        fields= (
            'nombre',
            'apellido',
            'telefono',
            'departamento',
            'ciudad',
            'direccion',
            'email',
            'descripcion',
            'experiencia',
            'contraseña'
        )

# REGISTRO DEPARTAMENTOS
class RegistroDepartamentoserializers(serializers.ModelSerializer):

    class Meta:
        model = Departamentos
        fields= "__all__"
#REGISTRO LOCALIDADES
class RegistroLocalidadeserializers(serializers.ModelSerializer):

    class Meta:
        model = Localidades
        fields = "__all__"