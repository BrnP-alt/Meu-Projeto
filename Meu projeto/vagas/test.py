from django.test import TestCase
from .models import Vaga

class VagaModelTest(TestCase):
    def test_criacao_vaga(self):
        vaga = Vaga.objects.create(numero=1, tipo='Carro')
        self.assertEqual(vaga.numero, 1)
        self.assertFalse(vaga.ocupada)

        from django.test import TestCase
from .models import Vaga

class VagaModelTest(TestCase):
    def test_cria_vaga_livre(self):
        vaga = Vaga.objects.create(numero=1, tipo='Carro')
        self.assertFalse(vaga.ocupada)

