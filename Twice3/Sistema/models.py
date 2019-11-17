from django.db import models
from django.contrib.auth.models import User



class Persona(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nombrePersona=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    tipoPersona=models.CharField(max_length=50, default='Usuario')

