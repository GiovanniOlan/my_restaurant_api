from rest_framework.routers import DefaultRouter
from apps.users.api.api import *

router = DefaultRouter()

router.register(r'user-owner',UserOwnerViewSet,basename='users')

urlpatterns = router.urls 