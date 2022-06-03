from rest_framework.routers import DefaultRouter
from apps.users.api.api import *

router = DefaultRouter()

router.register(r'user',UserSerializer,basename='users')

urlpatterns = router.urls 