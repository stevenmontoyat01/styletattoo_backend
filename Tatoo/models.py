from datetime import datetime
from email.policy import default
from tkinter import image_names
from django.db import models
from .choices import generos

#Table departament (departamentos)
class Departament (models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
#Table Locaties (localidades o ciudades)
class Locaties(models.Model):
    Fk_departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
#Table Users (usuarios)
class Users (models.Model):
    Id_user = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    CellPhone = models.TextField()
    Email = models.TextField(max_length=90)
    Password = models.TextField(max_length=20)
    Rol = models.CharField(default='[ROLE_USUARIO]',max_length=20)
    image = models.ImageField()
    Condition = models.CharField(default=1, max_length=1)

    def name_User(self):
        return "{} {}".format(self.Name,self.LastName)

    def __str__(self):
        return self.name_User()

#Table Tattoo artist (Tatuadores)
class Tattoo_artist (models.Model):
    Id_artist = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Cellphone = models.TextField()
    Departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    Locaties = models.ForeignKey(Locaties, on_delete=models.CASCADE)
    Direction = models.TextField()
    Email = models.TextField(max_length=90)
    Experience = models.CharField(max_length=3)
    Description=models.TextField(max_length=150,blank=True,default='')
    Password = models.TextField(max_length=20)
    Rol = models.CharField(default='[ROLE_TATUADOR]',max_length=20)
    image = models.ImageField()
    Condition = models.CharField(default='A', max_length=1)

    def name_artist(self):
        return "{} {}".format(self.Name,self.LastName)

    def __str__(self):
        return self.name_artist()

#Table quotes (citas)
class Quotes(models.Model):
    Id_quotes = models.BigAutoField(primary_key=True)
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    Img = models.ImageField()
    Description = models.CharField(max_length=150, blank=False, default='')

#Table brifcase_artist (portafolio tatuador)
class briefcase_artist(models.Model):
    Id_briefcase = models.BigAutoField(primary_key=True)
    Date_publication = models.DateTimeField(default=datetime.now())
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    Img = models.ImageField()
    Description = models.TextField(max_length=150,blank=True,default='')

#Table likes (me gustas)
class likes(models.Model):
    Id_likes = models.BigAutoField(primary_key=True)
    Tattoo_artist = models.ForeignKey(Tattoo_artist, on_delete=models.CASCADE)
    Counter_likes = models.IntegerField()

