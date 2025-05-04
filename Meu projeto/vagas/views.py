from django.shortcuts import render, redirect, get_object_or_404
from .models import Vaga

def listar_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas/listar_vagas.html', {'vagas': vagas})

def ocupar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    vaga.ocupada = True
    vaga.save()
    return redirect('listar_vagas')

def liberar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    vaga.ocupada = False
    vaga.save()
    return redirect('listar_vagas')
