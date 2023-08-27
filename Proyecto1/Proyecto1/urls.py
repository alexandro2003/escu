"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from app1.views import iniciar_sesion_view, registro_view, codigocarrera_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro_view, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion_view, name='iniciar_sesion'),
    path('inicio', views.inicio_view, name='inicio'),
    path('avatar', views.avatar_view, name='avatar'),
    path('home', views.home_view, name='home'),
    path('perfil', views.perfil_view, name='perfil'),
    path('olvidocontraseña', views.olvidocontraseña_view, name='olvidocontraseña'),
    path('editarperfil', views.editarperfil_view, name='editarperfil'),
    path('codigocarrera', views.codigocarrera_view, name='codigocarrera'),
    path('cerrarsesion', views.cerrarsesion_view, name='cerrarsesion'),
    path('home', views.home_view, name='home'),
    path('inscripcionexamenes', views.inscripcionexamenes_view, name='inscripcionexamenes'),
    path('inscripcionexamenes2', views.inscripcionexamenes2_view, name='inscripcionexamenes2'),
    path('inscripcionmaterias', views.inscripcionmaterias_view, name='inscripcionmaterias'),
    path('inscripcionmaterias2', views.inscripcionmaterias2_view, name='inscripcionmaterias2'),
] 

