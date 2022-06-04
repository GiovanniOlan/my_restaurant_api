from django.db import models
from apps.base.models import BaseModel
from apps.users.models import UserOwner
from simple_history.models import HistoricalRecords


class Restaurant(BaseModel):
    
    res_name        = models.CharField('Nombre',max_length=30)
    res_description = models.TextField('Descripción')
    res_logo        = models.ImageField('Logo',null=True, blank=True)
    res_slogan      = models.CharField('Slogan',max_length=50)
    res_mainimage   = models.ImageField('Imagen Principal',null=True, blank=True)
    res_fkuserowner = models.ForeignKey(UserOwner,on_delete=models.CASCADE,db_column='res_fkuserowner',verbose_name='Propietario')
    usu_historical  = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  

    class Meta:
        """Meta definition for Restaurant"""
        db_table = 'RESTAURANT'
        verbose_name = 'Restaurantes'
        verbose_name_plural = 'Restaurante'

    def __str__(self):
        """Unicode representation of Restaurant"""
        return f'{self.res_name}'
    

class CategoryMenu(BaseModel):
    catmen_name         = models.CharField('Nombre',max_length=30) 
    catmen_description  = models.TextField('Descripción')
    catmen_fkrestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,db_column='catmen_fkrestaurant', verbose_name='Restaurante')
    catmen_historical  = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  
    class Meta:
        db_table            = 'CAT_MENU'
        verbose_name        = 'Categoría Del Menú'
        verbose_name_plural = 'Categorías Del Menú'

    def __str__(self):
        return  f'{self.catmen_name}'    
        

class CategoryMenuItem(BaseModel):
    catmenite_name        = models.CharField('Nombre',max_length=30)
    catmenite_description = models.TextField('Descripción')
    catmenite_for         = models.PositiveSmallIntegerField('Para Cantidad De Personas')
    catmenite_image       = models.ImageField('Imagen',upload_to='images/menu-item')
    catmenite_price       = models.DecimalField('Precio',max_digits=10, decimal_places=2)
    catmenite_fkcatmenu   = models.ForeignKey(CategoryMenu, on_delete=models.CASCADE,db_column='catmenite_fkcatmenu', verbose_name='Categoria')
    catmenite_historical  = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  
    class Meta:
        db_table            = 'CAT_MENU_ITEM'
        verbose_name        = 'Plato'
        verbose_name_plural = 'Platos'

    def __str__(self):
        return f'{self.catmenite_name}'