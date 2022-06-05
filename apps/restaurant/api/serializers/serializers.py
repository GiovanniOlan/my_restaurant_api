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