from rest_framework.routers import DefaultRouter
from apps.restaurant.api.viewsets.viewsets import RestaurantViewSet

router = DefaultRouter()

router.register(r'restaurants',RestaurantViewSet,basename='restaurants')

urlpatterns = router.urls 
