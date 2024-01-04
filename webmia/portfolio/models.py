from django.db import models

class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    media = models.FileField(upload_to="Proyects", default='default_value.mp4')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'


