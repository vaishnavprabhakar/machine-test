from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type':'password'})
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_fields = {
            "read_only" : True
        }
        
        
    def validate_confirm_password(self, value):
        print(value)
        password = value.get('password')
        confirm_password = value.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError("Password does not match")
        return value
