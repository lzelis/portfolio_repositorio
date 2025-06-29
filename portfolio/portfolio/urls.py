"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# portfolio/urls.py (el archivo de URLs principal)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin  # Agregar esta línea
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myportfolio.urls')),  # Cambia 'myportfolio' si es el nombre de tu app
]

# Esto permite servir los archivos de medios en el entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)