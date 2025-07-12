from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import experiencia_academica_view
from django.shortcuts import render

urlpatterns = [
    path('', views.about_me, name='about_me'),  # Página de inicio (Sobre mí)
    path('projects/', views.projects, name='projects'),  # Proyectos
    path('blog/', views.blog, name='blog'),  # Blog
    path('experiencia-academica/', experiencia_academica_view, name='experiencia_academica'),  # Cambié 'formacion' por 'academic-experience'
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
    path('contacto-enviado/', lambda request: render(request, 'mensaje_enviado.html'), name='mensaje_enviado'),
]

# Solo en desarrollo, servir imágenes desde la carpeta media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)