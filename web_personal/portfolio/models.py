from django.db import models


# Create your models here.
class Project(models.Model):
    """ Model per agregar projectes a la base de dades """
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        """
        Metadades de la clase per:
        verbose_name: Indicara el nom traduit
        verbose_name_plural: Indicara el nom traduit i en plural
        ordering = ['-created']: Ordenara els projectes per data de creació i en ordre de mes nou a mes vell
        """
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        """ Mostrara en comptes de nom raro per defecte, el nom del projecte a la llista """
        return self.title

