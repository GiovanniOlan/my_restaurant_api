from  rest_framework import serializers
from apps.restaurant.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ('state','created_date','modified_date','deleted_date')
        
    def validate_res_fkuserowner(self,value):
        value = self.context['userowner_logged']
        return value
    
    def to_representation(self,instance):
        response = super().to_representation(instance)
        del response['res_fkuserowner']
        return response

class CategoryMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMenu
        exclude = ('state','created_date','modified_date','deleted_date')
        
    # def validate_catmen_fkrestaurant(self,value):
    #     #value = self.context['restaurant_id']
    #     return self.restaurant_id
    
    # def to_representation(self,instance):
    #     response = super().to_representation(instance)
    #     del response['res_fkuserowner']
    #     return response
    
class CategoryMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMenuItem
        exclude = ('state','created_date','modified_date','deleted_date')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('state','created_date','modified_date','deleted_date')
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        exclude = ('state','created_date','modified_date','deleted_date')
        
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['emp_fkgender'] = instance.emp_fkgender.catgen_name
        response['emp_fkuser'] = {
            'id': instance.emp_fkuser.id,
            'username': instance.emp_fkuser.username,
            'email': instance.emp_fkuser.email,
        }
        return response
        
    # def validate_res_fkuserowner(self,value):
    #     value = self.context['userowner_logged']
    #     return value
    
    # def to_representation(self,instance):
    #     response = super().to_representation(instance)
    #     del response['res_fkuserowner']
    #     return response        

