from django.shortcuts import render, redirect
from .models import Vaga
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def listar_vagas(request):
    return render(request, 'vagas/listar_vagas.html')

@login_required
def ocupar_vaga(request, vaga_id):
    # Lógica para ocupar vaga
    return render(request, 'vagas/ocupar_vaga.html')

@login_required
def liberar_vaga(request, vaga_id):
    # Lógica para liberar vaga
    return render(request, 'vagas/liberar_vaga.html')


# Lista todas as vagas
def listar_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas/listar_vagas.html', {'vagas': vagas})

# Ocupar uma vaga
def ocupar_vaga(request, vaga_id):
    vaga = Vaga.objects.get(id=vaga_id)
    vaga.ocupada = True
    vaga.save()
    return redirect('listar_vagas')

# Liberar uma vaga
def liberar_vaga(request, vaga_id):
    vaga = Vaga.objects.get(id=vaga_id)
    vaga.ocupada = False
    vaga.save()
    return redirect('listar_vagas')
