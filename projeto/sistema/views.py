from django.shortcuts import render, redirect
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
