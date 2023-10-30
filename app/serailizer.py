from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style = {'confirm_password': 'password'})
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_fields = {
            "write_only" : True
        }
        
        
    def validate_confirm_password(self, value):
   
        password = value.get('password')
        confirm_password = value.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError("Password does not match")
        return value

    