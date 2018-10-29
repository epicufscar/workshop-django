from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'homt.html',{'alunos':alunos})


def adicionar(request):

    if request.method == "POST":
        nome = request.POST.get('nome')
        ra = request.POST.get('ra')
        aluno = Aluno.objects.create()
        aluno.nome = nome
        aluno.ra = ra
        aluno.trancou = False
        aluno.save()
        return redirect('home')

    return render(request, 'adicionar.html', {})


def remover(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('home')


def trancar(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.trancou = True
    aluno.save()
    return redirect('home')


def editar(request, id):
    aluno = get_object_or_404(Aluno, pk=id)

    if request.method == "POST":
        nome = request.POST.get('nome')
        ra = request.POST.get('ra')
        aluno.nome = nome
        aluno.ra = ra
        aluno.save()
        return redirect('home')

    return render(request, 'editar.html', {'aluno':aluno})
