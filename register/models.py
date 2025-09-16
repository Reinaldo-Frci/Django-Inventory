from django.db import models
from django.utils.functional import empty
from inventory.models import Equipamento


# Create your models here.
class Log(models.Model):
    timeout = models.DateTimeField(auto_now=True)
    timein = models.DateTimeField()
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='logs')
    nome = models.CharField(max_length=30)
    tempo = models.IntegerField()

    def __str__(self):
        if self.timein is empty:
            return f"{self.equipamento} foi retirado por {self.nome} no dia {self.timeout}"
        else:
            return f"{self.equipamento} foi devolvido por {self.nome} no dia {self.timein}"
