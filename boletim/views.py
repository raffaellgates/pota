from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
	# perfil = Perfil.objects.all()
	# perfil_logado = get_perfil_logado(request)

	# my_contatos = perfil_logado.contatos.all()
	# all_posts = Postagem.objects.all()
	# postagem = []
	# for post in all_posts:
	# 	if post.perfil in my_contatos or post.perfil == perfil_logado:
	# 		postagem.append(post)

	# paginator = Paginator(postagem,3)
	
	# try:
	# 	page = int(request.GET.get('page','1'))
	# except:
	# 	page = 1

	# try:
	# 	postagem = paginator.page(page)
	# except:
	# 	postagem = paginator.page(paginator.num_pages)

	return render(request, 'index.html')


def login(request):
	return render(request, 'login.html')


def get_perfil_logado(request):
	return request.user.perfil