from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)  # Aquí se especifica el campo para subir imágenes

    def __str__(self):
        return self.title

class Career(models.Model):
    year = models.IntegerField()
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    position = models.FloatField(default=0.0)  # Este es el campo que usas para la posición en la línea de tiempo
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # 🔹 NUEVO CAMPO
    def __str__(self):
        return f"{self.year} - {self.job_title} en {self.company}"

class AcademicExperience(models.Model):
    TIPO_CHOICES = [
        ('Universitario', 'Universitario'),
        ('Curso', 'Curso'),
        ('Certificación', 'Certificación'),
    ]

    MODALIDAD_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Online', 'Online'),
    ]

    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    modalidad = models.CharField(max_length=50, choices=MODALIDAD_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    image = models.ImageField(upload_to='formaciones/', null=True, blank=True)  # Aquí se especifica el campo para subir imágenes
    orden = models.PositiveIntegerField(default=0)  # para ordenar como quieras
    enlace = models.URLField(blank=True, null=True)  # 👈 nuevo campo

    class Meta:
        ordering = ['orden']  # se ordena por este campo

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"