from django.db import models
from apps.base.models import BaseModel
from apps.users.models import UserOwner
from simple_history.models import HistoricalRecords
from django.conf import settings
from apps.users.models import CategoryGender,CategoryRol


class Restaurant(BaseModel):
    
    res_name        = models.CharField('Nombre',max_length=30)
    res_description = models.TextField('Descripción')
    res_logo        = models.ImageField('Logo',null=True, blank=True)
    res_slogan      = models.CharField('Slogan',max_length=50)
    res_mainimage   = models.ImageField('Imagen Principal',upload_to='images/restaurant',null=True, blank=True)
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
    catmen_image   = models.ImageField('Imagen Principal',upload_to='images/category-menu',null=True, blank=True)
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
    catmenite_image       = models.ImageField('Imagen',upload_to='images/category-menu-item',null=True, blank=True)
    catmenite_price       = models.DecimalField('Precio',max_digits=10, decimal_places=2)
    catmenite_fkcatmenu   = models.ForeignKey(CategoryMenu,on_delete=models.CASCADE,db_column='catmenite_fkcatmenu', verbose_name='Categoria')
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
    
class Client(BaseModel):
    cli_name         = models.CharField('Nombre',max_length=30)
    cli_description  = models.TextField('Descripción')
    cli_address      = models.CharField('Dirección',max_length=255)
    cli_datebirth    = models.DateTimeField(verbose_name='Fecha De Nacimiento')
    cli_address      = models.CharField('Dirección',max_length=100,null=True,)
    cli_image        = models.ImageField('Imagen',upload_to='images/client',null=True, blank=True)
    cli_fkrestaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,db_column='cli_fkrestaurant', verbose_name='Restaurant')
    cli_historical   = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  
    class Meta:
        db_table            = 'CLIENT'
        verbose_name        = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.cli_name}'
    
class Empleado(BaseModel):
    emp_description  = models.TextField('Descripción')
    emp_curp         = models.CharField('CURP',max_length=100,null=True,)
    emp_rfc          = models.CharField('RFC',max_length=100,null=True,)
    emp_datebirth    = models.DateTimeField(verbose_name='Fecha De Nacimiento')
    emp_image        = models.ImageField('Imagen',upload_to='images/empleado',null=True, blank=True)
    emp_fkrol        = models.ForeignKey(CategoryRol,on_delete=models.CASCADE,default='1',db_column='emp_fkrol',verbose_name='Rol')
    emp_fkgender     = models.ForeignKey(CategoryGender, on_delete=models.CASCADE,default=2,db_column='emp_fkgender',verbose_name='Genero')
    emp_fkuser       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,db_column='emp_fkuser',verbose_name='User')
    emp_fkrestaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,db_column='emp_fkrestaurant', verbose_name='Restaurant')
    emp_historical   = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  
    class Meta:
        db_table            = 'EMPLEADO'
        verbose_name        = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.long_name()
    
    def long_name(self):
        return f'{self.emp_fkuser.first_name} {self.emp_fkuser.last_name}'