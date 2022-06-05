from rest_framework.routers import DefaultRouter
from apps.restaurant.api.viewsets.viewsets import *

router = DefaultRouter()

router.register(r'restaurants',RestaurantViewSet,basename='restaurants')
router.register(r'category-menu',CategoryMenuViewSet,basename='category-menu')

urlpatterns = router.urls 
