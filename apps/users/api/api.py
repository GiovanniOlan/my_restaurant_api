from rest_framework import status,viewsets
from rest_framework.response import Response
from apps.users.api.serializers import *
from apps.users.authentication_mixin import Authentication

class UserOwnerViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = UserOwnerSerializer
    serializer_class_second = UserSerializer
    queryset = serializer_class.Meta.model.objects.filter(state=True)

    def create(self,request):
        # if self.user_owner.has_role('owner'):
        if self.user.is_superuser==1:
            data = request.data
            authuser_serializer = self.serializer_class_second(data=data['auth_user'])
            if authuser_serializer.is_valid():
                auth_user = authuser_serializer.save()
                data['user_custom']['usu_fkuser'] = auth_user.id
                usercustom_serializer = self.serializer_class(data=data['user_custom'])
                if usercustom_serializer.is_valid():
                    usercustom_serializer.save()
                    return Response({'message': 'Usuario Creado Correctamente.'},status=status.HTTP_201_CREATED)
                
                delete_user = User.objects.filter(id=auth_user.id).first()
                delete_user.delete()
                return Response(usercustom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'No tienes autorización para este contenido.'},status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request,pk):
        print(self.user)
        #if self.user_owner.has_role('owner'):
        if self.user.is_superuser==1:
            instance_usercustom = self.serializer_class.Meta.model.objects.filter(state=True,id=pk).first()
            usercustom_serializer = self.serializer_class(instance_usercustom,data=request.data['user_custom'])
            if usercustom_serializer.is_valid():
                usercustom = usercustom_serializer.save()
                instance_authuser = User.objects.filter(id=usercustom.usu_fkuser.id).first()
                authuser_serializer = self.serializer_class_second(instance_authuser,data=request.data['auth_user'])
                print(authuser_serializer)
                if authuser_serializer.is_valid():
                    #self.perform_update(authuser_serializer)
                    authuser = authuser_serializer.save()
                    
                    return Response({'message': 'Usuario Actualizado Correctamente.'},status=status.HTTP_200_OK)
                return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                            
            return Response(usercustom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'No tienes autorización para este contenido.'},status=status.HTTP_401_UNAUTHORIZED)
        
    
        

        
# class UserClientViewSet(viewsets.ModelViewSet):
#     serializer_class = ClientSerializer
#     serializer_class_second = UserCustomSerializer
#     serializer_class_third = UserSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state=True)
    
#     def create(self,request):
#         data = request.data
#         errors = {}
#         authuser_serializer = self.serializer_class_third(data=data['auth_user'])
#         if authuser_serializer.is_valid():
#             auth_user = authuser_serializer.save()
#             data['user_custom']['usu_fkuser'] = auth_user.id
#             usercustom_serializer = self.serializer_class_second(data=data['user_custom'])
#             if usercustom_serializer.is_valid():
#                 usercustom = usercustom_serializer.save()
#                 data['client'] = {'cli_fkusercustom': usercustom.id} # here when i decide what field will have Client just change this for: data['client'][cli_fkusercustom] = usercustom.id 
#                 client_serializer = self.serializer_class(data=data['client'])
#                 if client_serializer.is_valid():
#                     client_serializer.save()
#                     return Response({'message': 'Cliente Creado Correctamente.'},status=status.HTTP_201_CREATED)
#                 errors['errors'] += client_serializer.errors
#                 delete_usercustom = self.get_queryset().filter(id=usercustom.id)
#                 delete_usercustom.delete()
#             errors['errors'] = usercustom_serializer.errors
#             delete_authuser = User.objects.filter(id=auth_user.id).first()
#             delete_authuser.delete()
#             return Response(usercustom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         errors['errors'] = authuser_serializer.errors
#         return Response(errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request,pk):
#         instance_client = self.serializer_class.Meta.model.objects.filter(state=True,id=pk).first()
#         instance_usercustom = self.serializer_class_second.Meta.model.objects.filter(state=True,id=instance_client.cli_fkusercustom.id).first()
#         usercustom_serializer = self.serializer_class_second(instance_usercustom,data=request.data['user_custom'])
        
#         if usercustom_serializer.is_valid():
#             usercustom = usercustom_serializer.save()
#             instance_authuser = User.objects.filter(id=usercustom.usu_fkuser.id).first()
#             authuser_serializer = self.serializer_class_third(instance_authuser,data=request.data['auth_user'])
#             if authuser_serializer.is_valid():
#                 authuser = authuser_serializer.save()
#                 return Response({'message': 'Usuario Actualizado Correctamente.'},status=status.HTTP_200_OK)
#             return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                        
#         return Response(usercustom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)