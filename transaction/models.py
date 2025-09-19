from django.db import models
from django.utils.functional import empty
from inventory.models import Equipamento, Local, Cabo


# Create your models here.


class LogSaida(models.Model):
    nome = models.CharField(max_length=30)
    equipamento = models.ManyToManyField(Equipamento, blank=True)
    cabo = models.ManyToManyField(Cabo, blank=True)
    timeout = models.DateTimeField(auto_now=True)
    timein = models.DateTimeField(null=True, blank=True)
    tempo = models.IntegerField()

    def __str__(self):
        if self.timein is empty:
            return f"{self.equipamento} foi retirado por {self.nome} no dia {self.timeout}"
        else:
            return f"{self.equipamento} {self.cabo} foi devolvido por {self.nome} no dia {self.timein}"

class LogMudarLocal(models.Model):
    nome = models.CharField(max_length=30)
    equipamento = models.ManyToManyField(Equipamento, blank=True)
    cabo = models.ManyToManyField(Cabo, blank=True)
    localfrom = models.ForeignKey(Local, on_delete=models.DO_NOTHING, related_name='logSaída')
    localto = models.ForeignKey(Local, on_delete=models.DO_NOTHING, related_name='logEntrada')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.equipamento} {self.cabo} foi transferido de {self.localfrom} para {self.localto} no dia {self.time}"