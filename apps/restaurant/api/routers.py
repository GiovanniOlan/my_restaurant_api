from rest_framework.routers import DefaultRouter
from apps.restaurant.api.viewsets.viewsets import *

router = DefaultRouter()

router.register(r'restaurants',RestaurantViewSet,basename='restaurants')
router.register(r'category-menu',CategoryMenuViewSet,basename='category_menu')
router.register(r'category-menu-item',CategoryMenuItemViewSet,basename='category_menu_item')
router.register(r'clients',ClientViewSet,basename='clients')
router.register(r'empleados',EmpleadoViewSet,basename='empleados')

urlpatterns = router.urls 
