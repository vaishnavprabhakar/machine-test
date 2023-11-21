from app.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.authentication import authenticate
from .tokens import get_tokens_for_user
from django.contrib.auth import login
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated  

# Create your views here.


class UserRegisterApi(APIView):
    
    def get(self, request):
        return Response({"msg": "Register"})
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            
            user = CustomUser.objects.create_user(
                username=serializer.validated_data.get('username'),
                email = serializer.validated_data.get('email'),
                password = serializer.validated_data.get('password')
            )
            
            return Response({"msg": "Registered successfully..."},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApi(APIView):
    
    def get(self, request):
        return Response({"msg": "Login"},status=200)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            token = get_tokens_for_user(user=user)
            return Response({"token" : token, "msg": "Login Sucessfull"},
                            status=status.HTTP_200_OK)
        return Response({"msg": "Something got wrong or you must check your credentials"},
                        status=status.HTTP_400_BAD_REQUEST)
    
    @authentication_classes([IsAuthenticated])
    def put(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg" : "Profile updated...", "data": serializer.data},
                status=status.HTTP_200_OK
                )
        return Response(
            {"msg": serializer.errors}
            )
        
    
# this is rough.

'''
Hai, hello nice to meet you. im a passionate software developer who focus on django which is beackend framework for python language..
'''