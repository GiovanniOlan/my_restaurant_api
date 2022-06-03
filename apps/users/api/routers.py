from rest_framework.routers import DefaultRouter
from apps.users.api.api import *

router = DefaultRouter()

router.register(r'user-owner',UserOwnerViewSet,basename='users')
router.register(r'client',UserClientViewSet,basename='client')

urlpatterns = router.urls 