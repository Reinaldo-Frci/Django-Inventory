import uuid

from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=7)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} | {self.email} "