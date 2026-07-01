from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    ROLES = [
        ('admin', 'Admin'),
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionario'),
        ('cliente', 'Cliente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"