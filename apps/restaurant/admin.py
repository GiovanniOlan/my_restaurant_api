from django.contrib import admin
from apps.restaurant.models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(CategoryMenu)
admin.site.register(CategoryMenuItem)
