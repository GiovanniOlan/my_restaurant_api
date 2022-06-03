from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
from django.conf import settings


# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
#         user = self.model(
#             username = username,
#             email = email,
#             name = name,
#             last_name = last_name,
#             is_staff = is_staff,
#             is_superuser = is_superuser,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, username, email, name,last_name, password=None, **extra_fields):
#         return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

#     def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
#         return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length = 255, unique = True)
#     email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
#     name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
#     last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
#     image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
#     is_active = models.BooleanField(default = True)
#     is_staff = models.BooleanField(default = False)
#     is_premium = models.BooleanField(default = False)
#     historical = HistoricalRecords()
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email','name','last_name']

#     def __str__(self):
#         return f'{self.name} {self.last_name}'
    

class CategoryGender(BaseModel):
    catgen_name        = models.CharField('Nombre',max_length=30)
    catgen_description = models.CharField('Descripción',max_length=50)
    catgen_historical  = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  
    class Meta:
        """Meta definition for CategoryGender"""
        db_table = 'CAT_GENDER'
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
    def __str__(self):
        """Unicode representation of CategoryGender"""
        return f'{self.catgen_name}'
    
class UserCustom(BaseModel):
    usu_fkgender   = models.ForeignKey(CategoryGender, on_delete=models.CASCADE,db_column='usu_fkgender',verbose_name='Genero')
    usu_datebirth  = models.DateTimeField(verbose_name='Fecha De Nacimiento')
    usu_address    = models.CharField('Dirección',max_length=255)
    usu_premium    = models.BooleanField('Premium',default = False)
    usu_fkuser     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='',db_column='usu_fkuser',verbose_name='User')
    usu_historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value  

    class Meta:
        """Meta definition for UserCustom"""
        db_table = 'USER_CUSTOM'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """Unicode representation of UserCustom"""
        return f'{self.usu_fkuser}'
    
    def short_name(self):
        return  f'{self.usu_fkuser.first_name}'
    
    def long_name(self):
        return f'{self.usu_fkuser.first_name} {self.usu_fkuser.last_name}'
    
# class Client(BaseModel):
#     cli_fkusercustom  = models.ForeignKey(UserCustom, on_delete=models.CASCADE,db_column='cli_fkusercustom',verbose_name='Usuario')
#     usu_historical = HistoricalRecords()

#     @property
#     def _history_user(self):
#         return self.changed_by

#     @_history_user.setter
#     def _history_user(self,value):
#         self.changed_by = value  
#     class Meta:
#         """Meta definition for Client"""
#         db_table = 'CLIENTS'
#         verbose_name = 'Cliente'
#         verbose_name_plural = 'Clientes'

#     def __str__(self):
#         """Unicode representation of Client"""
#         return f'{self.cli_fkusercustom.long_name}'