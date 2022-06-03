from django.db import models
from apps.base.models import Basemodel

# Create your models here.
class Restaurant(BaseModel):
    
    res_name        = models.CharField('Nombre',max_length=50)
    res_description = models.TextField('Descripción')
    res_logo        = models.ImageField('Logo',null=True, blank=True)
    res_slogan      = models.CharField('Slogan',max_length=50)
    res_mainimage   = models.ImageField('Imagen Principal',null=True, blank=True)
    res_fkUser

    class Meta:
        """Meta definition for Restaurant"""
        db_table = 'RESTAURANT'
        verbose_name = 'Restaurantes'
        verbose_name_plural = 'Restaurante'

    def __str__(self):
        """Unicode representation of Restaurant"""
        