import uuid

from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('taken', 'Retirado'),
    ('inventory', 'Em Inventário'),
)

class Local(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=6)
    nome = models.CharField(max_length=30)


    def __str__(self):
        return self.nome

class Cabo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=6)
    tipo = models.CharField(max_length=20)
    comprimento = models.IntegerField()
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, related_name='Equipamento', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inventory')

    def __str__(self):
        return f"Cabo {self.tipo} de {self.comprimento}M"


class Equipamento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=6)
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, related_name='Cabos', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inventory')

    def __str__(self):
        return f"{self.nome} da {self.marca} modelo {self.modelo}"

