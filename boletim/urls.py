from django.contrib import admin
from django.urls import path
from boletim import views as views_boletim
from django.contrib.auth import views as v

urlpatterns = [
    # Perfil.views
    path('admin/', admin.site.urls),
    path('', views_boletim.index, name='index'),
    path('login/',v.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('name/<int:user_id>/convidar',views.Lis, name='convidar'),
]