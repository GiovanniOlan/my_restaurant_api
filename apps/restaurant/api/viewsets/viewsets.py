from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.users.authentication_mixin import Authentication
from rest_framework.response import Response
from apps.restaurant.api.serializers.serializers import RestaurantSerializer



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
            
    def update(self,request):
        if self.user_owner.has_role('owner'):
            return super().update(request)
        else:
            return Response({'mensaje': 'No tienes permitido actualizar restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self,request,pk):
        if self.user_owner.has_role('owner'):
            restaurant = self.get_queryset().filter(id = pk).first()
            print(restaurant)
            if restaurant:
                restaurant.state = False
                restaurant.save()
            return Response({'mensaje': 'Se ha eliminado correctamente'}, status=status.HTTP_401_UNAUTHORIZED)
            #return super().destroy(request)
        else:
            return Response({'mensaje': 'No tienes permitido eliminar restaurantes.'}, status=status.HTTP_401_UNAUTHORIZED)
