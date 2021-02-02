from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import redirect
from .models import Aluno, Nota, Professor
from .forms import NotaModelForm

@login_required
def ListNotas(request, aluno_id=1):
    prof = Professor.objects.filter(usuario=request.user)
    if prof:
        notas = Nota.objects.all()
        return render(request, 'listNotas.html',
                  {'notas': notas})
    else:
        aluno = Aluno.objects.get(id=aluno_id)
        notas= Nota.objects.filter(alunoId=aluno)
        return render(request, 'listNotas.html', {'notas': notas})
    


@login_required
def index(request):
    professor = False
    if Professor.objects.filter(usuario=request.user):
        professor = True

    return render(request, 'index.html', {'perfil_logado': get_perfil_logado(request), 'professor': professor})

def get_perfil_logado(request):
    aluno = Aluno.objects.filter(usuario=request.user)
    if aluno:
        return request.user.aluno
    else:
        return request.user.professor


@login_required
def notasRegister(request):
    if request.method == "POST":
        form = NotaModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
        return redirect('index')

    else:
        form = NotaModelForm()
        return render(request,'notasDetails.html',{'form': form})