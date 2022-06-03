import re
from rest_framework import serializers
from apps.users.models import *
from django.contrib.auth.models import User


        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user  

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGender
        exclude = ('state','created_date','modified_date','deleted_date')
        
class UserCustomSerializer(serializers.ModelSerializer):
    #usu_fkuser   = UserSerializer()
    #usu_fkgender = serializers.StringRelatedField()
    
    class Meta:
        model   = UserCustom
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['usu_fkgender'] = instance.usu_fkgender.catgen_name
        response['usu_fkuser'] = {
            'id': instance.usu_fkuser.id,
            'username': instance.usu_fkuser.username,
            'email': instance.usu_fkuser.email,
        }
        return response

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         exclude = ('state','created_date','modified_date','deleted_date')
    
        
    
    
    # def create(self,validated_data):
    #     user = User(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    
    # def update(self,instance,validated_data):
    #     updated_user = super().update(instance,validated_data)
    #     updated_user.set_password(validated_data['password'])
    #     updated_user.save()
    #     return updated_user        