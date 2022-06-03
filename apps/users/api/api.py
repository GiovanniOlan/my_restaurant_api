from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
#from apps.users.models import User
from apps.users.api.serializers import *
from rest_framework import viewsets


# class UserAPIView(APIView):
#     def get(self, request,pk=None):
#         if pk is None:
#             users = User.objects.all()
#             users_serializer = UserSerializer(users,many = True)
#             return Response(users_serializer.data)
#         user = User.objects.filter(id = pk).first()
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data,status=status.HTTP_200_OK)    
        
#     def post(self, request):
#         user_serializer = UserSerializer(data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response({'message': 'Usuario Creado Correctamente.'},status=status.HTTP_201_CREATED)
        
#         return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request,pk):
#         user = User.objects.filter(id=pk).first()
#         user_serializer = UserSerializer(user,data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response({'message': 'Usuario Actualizado Correctamente'})
#         return Response({'message': 'El usuario no se pudo actualizar, verifica los datos.',},status=status.HTTP_400_BAD_REQUEST)\
    
class UserCustomViewSet(viewsets.ModelViewSet):
    serializer_class = UserCustomSerializer
    queryset = UserCustomSerializer.Meta.model.objects.filter()
    
            
    
class UserSerializer(viewsets.ModelViewSet):
    serializer_class = UserCustomSerializer
    serializer_class_second = UserSerializer
    queryset = serializer_class.Meta.model.objects.filter(state=True)
    
    # def get_queryset(self, pk=None):
    #     if pk is None:
    #         b = self.get_serializer().Meta.model.objects.filter(state=True)
    #         #print(b)
    #         return b
    #     a = self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
    #     print(f'No trae pk: {a}')
    #     return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    # def list(self,request):
        
        
    
    def create(self,request):
        data = request.data
        #print(data['auth_user'])
        authuser_serializer = self.serializer_class_second(data=data['auth_user'])
        if authuser_serializer.is_valid():
            auth_user = authuser_serializer.save()
            #print(f'IDDDDDDDDDDd {auth_user.id}')
            data['user_custom']['usu_fkuser'] = auth_user.id
            usercustom_serializer = self.serializer_class(data=data['user_custom'])
        
            print(f'USERCUSTOM ::::{usercustom_serializer}')
            if usercustom_serializer.is_valid():
                usercustom_serializer.save()
                return Response({'message': 'Usuario Creado Correctamente.'},status=status.HTTP_201_CREATED)
            
            delete_user = self.get_queryset().filter(id=auth_user.id)
            delete_user.delete()
            return Response(usercustom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
