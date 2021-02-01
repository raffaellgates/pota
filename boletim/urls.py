from django.contrib import admin
from django.urls import path
from boletim import views as views_boletim

urlpatterns = [
    # Perfil.views
    path('admin/', admin.site.urls),
    path('', views_boletim.index, name='index'),
<<<<<<< HEAD
    path('login/', views_boletim.login, name='login'),
=======
    path('/login', views_boletim.login, name='login'),
>>>>>>> fb7491ee821e03c946d50f6ff8a1f32f63944efe
]