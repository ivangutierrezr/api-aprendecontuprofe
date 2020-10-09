"""aprendecontuprofeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from docente import views as viewsDocente
from estudiante import views as viewsEstudiante
from asignatura import views as viewsAsignatura
from sesiones import views as viewsSesiones

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login/$', viewsSesiones.iniciar_sesion),
    url(r'^api/logout/$', viewsSesiones.cerrar_sesion),
    url(r'^api/docentes/$', viewsDocente.docentes_manager),
    url(r'^api/docente/(?P<pk>[0-9]+)$', viewsDocente.docente_manager),
    url(r'^api/estudiantes/$', viewsEstudiante.estudiantes_manager),
    url(r'^api/estudiante/(?P<pk>[0-9]+)$', viewsEstudiante.estudiante_manager),
    url(r'^api/asignaturas/$', viewsAsignatura.asignaturas_manager),
    url(r'^api/asignatura/(?P<pk>[0-9]+)$', viewsAsignatura.asignatura_manager),
    url(r'^api/asignaturaestudiantes/(?P<pk>[0-9]+)$', viewsAsignatura.asignatura_manager_estudiantes),
    url(r'^api/asignaturasusuario/$', viewsAsignatura.asignaturas_usuario),
    url(r'^api/asignaturaitems/(?P<pk>[0-9]+)$', viewsAsignatura.items_asignatura),
]
