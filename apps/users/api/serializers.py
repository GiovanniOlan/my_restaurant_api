import re
from rest_framework import serializers
from apps.users.models import *
from django.contrib.auth.models import User


        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password','is_superuser']
        fields = '__all__'
        #fields = ['username', 'email', 'password']
        #read_only_fields = ['is_superuser']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGender
        exclude = ('state','created_date','modified_date','deleted_date')
        
class UserCustomSerializer(serializers.ModelSerializer):
    #usu_fkuser   = UserSerializer()
    usu_fkgender = serializers.StringRelatedField()
    
    class Meta:
        model   = UserCustom
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        print(type(response))
        response['usu_fkuser'] = {
            'id': instance.usu_fkuser.id,
            'username': instance.usu_fkuser.username,
            'email': instance.usu_fkuser.email,
        }
        return response
    
    
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