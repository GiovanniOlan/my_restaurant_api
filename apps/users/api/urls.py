from django.urls import path, include
# from apps.users.api.api import UserAPIView

urlpatterns = [
    # path('<int:pk>',UserAPIView.as_view(), name = 'one_user'),
    # path('',UserAPIView.as_view(), name = 'all_users'),
    # # path('<int:pk>',UserEspecified.as_view(), name = 'one_user')
    path('', include('apps.users.api.routers'))
]