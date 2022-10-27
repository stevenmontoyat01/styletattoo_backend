#Libraries
import email
from imaplib import _Authenticator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import Users,Tattoo_artist,Quotes,Departament,Locaties,likes,briefcase_artist


#METHOD POST

#FORMULARIO REGISTROS CITAS
class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields= "__all__"

# FORMULATIO REGISTRO PORTAFOLIO
class Briefcase_ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model= briefcase_artist
        fields=(
            'tatuador',
            'imagen',
            'descripcion'
        )

#------------------------------------------------------------------------------------------
# FORMULARIOS  REGISTROS USUARIOS

class UsersModelSerializers(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=50)
    LastName = serializers.CharField(max_length=50)
    Password = serializers.CharField(max_length=20)
    Email = serializers.CharField(max_length=90)
    CellPhone = serializers.CharField(max_length=50)

    class Meta:
        model= Users
        fields= [
            "Name",
            "LastName",
            "CellPhone",
            "Password",
            "Email"
        ]

    def validate(self, attrs):
        email_exist = Users.objects.filter(Email=attrs["Email"]).exists()

        if email_exist:
            raise ValidationError("email has already been used")

        return super().validate(attrs)


#--------------------------------------------------------------------------------------------
# FORMULARIOS REGISTROS TATUADORES
class Tattoo_ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model= Tattoo_artist
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

#-------------------------------------------------------------------------------------------
# REGISTRO DEPARTAMENTOS
class DepartamentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields= "__all__"
#REGISTRO LOCALIDADES
class LocatiesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Locaties
        fields = "__all__"


#METHOD GET

class GetUsers(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'Id_user',
            'Name',
            'LastName',
            'Email',
            'Password'
        )

class GetArtist(serializers.ModelSerializer):

    class Meta:
        model = Tattoo_artist
        model = (
            'Id_artist',
            'Name'
        )