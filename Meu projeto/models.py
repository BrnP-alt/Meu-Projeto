from django.db import models

class Vaga(models.Model):
    numero = models.IntegerField(unique=True)  # Número da vaga
    ocupada = models.BooleanField(default=False)  # Se a vaga está ocupada
    tipo = models.CharField(max_length=10)  # Tipo de veículo, ex: "Carro", "Moto"

    def __str__(self):
        return f'Vaga {self.numero} - {"Ocupada" if self.ocupada else "Livre"}'
