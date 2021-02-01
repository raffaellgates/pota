from django.contrib import admin
from django.urls import path
from boletim import views as views_boletim

urlpatterns = [
    # Perfil.views
    path('admin/', admin.site.urls),
    path('', views_boletim.index, name='index'),
    path('/login', views_boletim.login, name='login'),
]