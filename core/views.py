from django.shortcuts import render, redirect
from .models import Evento, Presenca, Comentario


def home(request):
    eventos = Evento.objects.all().order_by('data')

    return render(request, 'home.html', {
        'eventos': eventos
    })


def criar_evento(request):
    if request.method == 'POST':

        Evento.objects.create(
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            local=request.POST.get('local'),
            data=request.POST.get('data'),
            horario=request.POST.get('horario'),
            categoria=request.POST.get('categoria'),
            vagas=request.POST.get('vagas'),
        )

    return redirect('home')


def confirmar_presenca(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':

        Presenca.objects.create(
            evento=evento,
            nome_aluno=request.POST.get('nome_aluno'),
            email=request.POST.get('email'),
        )

    return redirect('home')


def comentar(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':

        Comentario.objects.create(
            evento=evento,
            nome=request.POST.get('nome'),
            texto=request.POST.get('texto'),
        )

    return redirect('home')