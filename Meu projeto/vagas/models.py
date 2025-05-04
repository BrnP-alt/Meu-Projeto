from django.db import models

class Vaga(models.Model):
    numero = models.IntegerField(unique=True)
    ocupada = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10)  # Ex: "Carro", "Moto"

    def __str__(self):
        return f'Vaga {self.numero} - {"Ocupada" if self.ocupada else "Livre"}'
