import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "lzelis"
email = "leopoldozelis@gmail.com"
password = "virginia123"

if not User.objects.filter(username=username).exists():
    print("Creando superusuario...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("El superusuario ya existe.")