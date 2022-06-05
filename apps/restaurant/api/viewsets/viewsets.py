from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.users.authentication_mixin import Authentication
from rest_framework.response import Response
from apps.restaurant.api.serializers.serializers import *
from apps.users.api.serializers import UserSerializer
from django.contrib.auth.models import User



class RestaurantViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    #queryset = serializer_class.Meta.model.objects.filter(state=True)
    
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = {'userowner_logged':self.user_owner}
        return super().get_serializer(*args, **kwargs)
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True,res_fkuserowner=self.user_owner.id)
        return self.get_serializer().Meta.model.objects.filter(id=pk, res_fkuserowner=self.user_owner.id ,state=True).first()
    
    def list(self, request):
        if self.user_owner.has_role('owner'):
            restaurant_serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(restaurant_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'No tienes permitido ver restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
    def create(self,request):
        if self.user_owner.has_role('owner'):
            # self.serializer_class.get_context['userowner_logged_id'] = self.user_owner.id
            return super().create(request)
        else:
            return Response({'mensaje': 'No tienes permitido crear restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def update(self,request,pk):
        if self.user_owner.has_role('owner'):
            return super().update(request,partial=True)
        else:
            return Response({'mensaje': 'No tienes permitido actualizar restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self,request,pk):
        if self.user_owner.has_role('owner'):
            restaurant = self.get_queryset().filter(id = pk).first()
            print(restaurant)
            if restaurant:
                restaurant.state = False
                restaurant.save()
                return Response({'mensaje': 'Se ha eliminado correctamente.'}, status=status.HTTP_401_UNAUTHORIZED)
            #return super().destroy(request)
            return Response({'mensaje': 'No se ha encontrado ese Restaurante.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'mensaje': 'No tienes permitido eliminar restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)


class CategoryMenuViewSet(Authentication, viewsets.ModelViewSet):
    
    serializer_class = CategoryMenuSerializer
    
    def get_queryset(self,catmen_fkrestaurant=None):
        if catmen_fkrestaurant is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True,catmen_fkrestaurant=catmen_fkrestaurant)
    
    def list(self, request):
        if self.user_owner.has_role('owner'):
            try:
                catmen_fkrestaurant = request.data['catmen_fkrestaurant']
                print(catmen_fkrestaurant)
                restaurant_serializer = self.get_serializer(self.get_queryset(catmen_fkrestaurant), many=True)
                return Response(restaurant_serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'mensaje': 'No se han enviado los datos necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': 'No tienes permitido ver categorias.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def create(self,request):
        if self.user_owner.has_role('owner'):
            return super().create(request)
        else:
            return Response({'mensaje': 'No tienes permitido crear categorias.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def update(self,request,pk):
        if self.user_owner.has_role('owner'):
            return super().update(request,partial=True)
        else:
            return Response({'mensaje': 'No tienes permitido actualizar categorias.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self,request,pk):
        if self.user_owner.has_role('owner'):
            category_menu = self.get_queryset().filter(id = pk).first()
            if category_menu:
                category_menu.state = False
                category_menu.save()
                return Response({'mensaje': 'Se ha eliminado correctamente'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'mensaje': 'No se ha encontrado esa Categoria.'}, status=status.HTTP_404_NOT_FOUND)
            #return super().destroy(request)
        else:
            return Response({'mensaje': 'No tienes permitido eliminar categorias.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
class CategoryMenuItemViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = CategoryMenuItemSerializer
    
    def get_queryset(self,catmenite_fkcatmenu=None):
        if catmenite_fkcatmenu is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True,catmenite_fkcatmenu=catmenite_fkcatmenu)
    
    def list(self, request):
        if self.user_owner.has_role('owner'):
            try:
                catmenite_fkcatmenu = request.data['catmenite_fkcatmenu']
                restaurant_serializer = self.get_serializer(self.get_queryset(catmenite_fkcatmenu), many=True)
                return Response(restaurant_serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'mensaje': 'No se han enviado los datos necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': 'No tienes permitido ver platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def create(self,request):
        if self.user_owner.has_role('owner'):
            return super().create(request)
        else:
            return Response({'mensaje': 'No tienes permitido crear platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def update(self,request,pk):
        if self.user_owner.has_role('owner'):
            return super().update(request,partial=True)
        else:
            return Response({'mensaje': 'No tienes permitido actualizar platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self,request,pk):
        if self.user_owner.has_role('owner'):
            category_menu_item = self.get_queryset().filter(id = pk).first()
            if category_menu_item:
                category_menu_item.state = False
                category_menu_item.save()
                return Response({'mensaje': 'Se ha eliminado correctamente'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'mensaje': 'No se ha encontrado esa Categoria.'}, status=status.HTTP_404_NOT_FOUND)
            #return super().destroy(request)
        else:
            return Response({'mensaje': 'No tienes permitido eliminar platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class ClientViewSet(Authentication, viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    
    def get_queryset(self,cli_fkrestaurant=None):
        if cli_fkrestaurant is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True,cli_fkrestaurant=cli_fkrestaurant)
    
    def list(self, request):
        if self.user_owner.has_role('owner'):
            try:
                cli_fkrestaurant = request.data['cli_fkrestaurant']
                restaurant_serializer = self.get_serializer(self.get_queryset(cli_fkrestaurant), many=True)
                return Response(restaurant_serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'mensaje': 'No se han enviado los datos necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': 'No tienes permitido ver platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def create(self,request):
        if self.user_owner.has_role('owner'):
            return super().create(request)
        else:
            return Response({'mensaje': 'No tienes permitido crear platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def update(self,request,pk):
        if self.user_owner.has_role('owner'):
            return super().update(request,partial=True)
        else:
            return Response({'mensaje': 'No tienes permitido actualizar platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self,request,pk):
        if self.user_owner.has_role('owner'):
            client = self.get_queryset().filter(id = pk).first()
            if client:
                client.state = False
                client.save()
                return Response({'mensaje': 'Se ha eliminado correctamente'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'mensaje': 'No se ha encontrado esa Categoria.'}, status=status.HTTP_404_NOT_FOUND)
            #return super().destroy(request)
        else:
            return Response({'mensaje': 'No tienes permitido eliminar platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class EmpleadoViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    serializer_class_second = UserSerializer
    #queryset = serializer_class.Meta.model.objects.filter(state=True)
    
    def get_queryset(self,emp_fkrestaurant=None):
        if emp_fkrestaurant is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(state=True,emp_fkrestaurant=emp_fkrestaurant)
    
    def list(self, request):
        if self.user_owner.has_role('owner'):
            try:
                emp_fkrestaurant = request.data['emp_fkrestaurant']
                restaurant_serializer = self.get_serializer(self.get_queryset(emp_fkrestaurant), many=True)
                return Response(restaurant_serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'mensaje': 'No se han enviado los datos necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mensaje': 'No tienes permitido ver platillos.'}, status=status.HTTP_401_UNAUTHORIZED)
        

    def create(self,request):
        # if self.user_owner.has_role('owner'):
        if self.user_owner.has_role('owner'):
            data = request.data
            authuser_serializer = self.serializer_class_second(data=data['auth_user'])
            if authuser_serializer.is_valid():
                auth_user = authuser_serializer.save()
                data['empleado']['emp_fkuser'] = auth_user.id
                empleado_serializer = self.serializer_class(data=data['empleado'])
                if empleado_serializer.is_valid():
                    empleado_serializer.save()
                    return Response({'message': 'Usuario Creado Correctamente.'},status=status.HTTP_201_CREATED)
                
                delete_user = User.objects.filter(id=auth_user.id).first()
                delete_user.delete()
                return Response(empleado_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'No tienes autorización para este contenido.'},status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request,pk):
        print(self.user)
        #if self.user_owner.has_role('owner'):
        if self.user_owner.has_role('owner'):
            instance_empleado = self.serializer_class.Meta.model.objects.filter(state=True,id=pk).first()
            empleado_serializer = self.serializer_class(instance_empleado,data=request.data['empleado'])
            if empleado_serializer.is_valid():
                empleado = empleado_serializer.save()
                instance_authuser = User.objects.filter(id=empleado.emp_fkuser.id).first()
                authuser_serializer = self.serializer_class_second(instance_authuser,data=request.data['auth_user'])
                print(authuser_serializer)
                if authuser_serializer.is_valid():
                    #self.perform_update(authuser_serializer)
                    authuser = authuser_serializer.save()
                    
                    return Response({'message': 'Usuario Actualizado Correctamente.'},status=status.HTTP_200_OK)
                return Response(authuser_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                            
            return Response(empleado_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'No tienes autorización para este contenido.'},status=status.HTTP_401_UNAUTHORIZED)
