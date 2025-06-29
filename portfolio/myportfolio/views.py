from django.shortcuts import render
from .models import Project  # Importa el modelo Project
from .models import Career
from .models import AcademicExperience
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

# Vista para la sección "Sobre mí"
def about_me(request):
    careers = Career.objects.all()  # Obtener todas las trayectorias
    return render(request, 'about_me.html', {'careers': careers})

# Vista para la sección "Proyectos"
def projects(request):
    projects = Project.objects.all()  # Obtiene todos los proyectos
    return render(request, 'projects.html', {'projects': projects})

# Vista para la sección "Blog"
def blog(request):
    return render(request, 'blog.html')

# Vista para la sección "Contacto"
def contact(request):
    return render(request, 'contact.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Nombre: {name}\nEmail: {email}\n\n{message}"

        send_mail(
            subject='Nuevo mensaje desde el portfolio',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],  # Agregalo en settings.py
        )

        return HttpResponseRedirect('/contacto-enviado/')  # Redirige a una página de confirmación

    return HttpResponseRedirect('/contact/')  # Redirige si alguien entra por GET

def experiencia_academica_view(request):
    formaciones = AcademicExperience.objects.all()
    return render(request, 'experiencia_academica.html', {'formaciones': formaciones})