from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.
class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data=request.data,context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            token,created = Token.objects.get_or_create(user=user)
            if not created:
                token.delete()
                token = Token.objects.create(user=user)

            return Response({
                'token': token.key,
                'mensaje': 'Inicio De Sesión Exitoso',
            }, status=status.HTTP_200_OK)    
                
                
        else:
            return Response({'mensaje': 'Nombre de usuarios o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

# class Logout(APIView):
#     def get(self, request, *args, **kwargs):
#         token = request.GET.get('token')
#         User  = Token.objects.filter(key=token).first()
         