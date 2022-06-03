from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado',default=True)
    created_date = models.DateField('Fecha De Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha De Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha De Creación', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel"""
        abstract = True
        verbose_name = 'ModeloBase'
        verbose_name_plural = 'Modelos Base'