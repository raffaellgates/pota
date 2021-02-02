from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import redirect
from .models import Aluno, Nota, Professor
from .forms import NotaModelForm

@login_required
def ListNotas(request, aluno_id=1):
    prof = Professor.objects.filter(usuario=request.user)
    if prof:
        notas = Aluno.objects.all()
        return render(request, 'listNotas.html',
                  {'notas': notas})
    
    aluno = Aluno.objects.filter(id=aluno_id)
    notas= Nota.objects.filter(alunoId=aluno)
    return render(request, 'listNotas.html',
                  {'notas': notas})
    


@login_required
def index(request):

    return render(request, 'index.html', {'perfil_logado': get_perfil_logado(request)})

def login(request):
	return render(request, 'login.html')


def get_perfil_logado(request):
    aluno = Aluno.objects.filter(usuario=request.user)
    if aluno:
        return request.user.aluno
    else:
        return request.user.professor

@login_required
def notasRegister(request):
    if request.method == 'POST':
        form = NotaModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            return render(request,'index.html')
    else:
        form_class = NotaModelForm
    return render(request,'notasDetails.html',{
    	'form': form_class,
    	})