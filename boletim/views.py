from django.shortcuts import render
from django.views.generic import View
from timeline.forms import PublicarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from models import Aluno, Nota


def ListNotas(request, aluno_id):
    aluno = Aluno.objects.filter(id=aluno_id)
    boletim = Nota.objects.filter(alunoID)

    return render(request, 'notasAlunos.html',
                  {'boletim': boletim})


