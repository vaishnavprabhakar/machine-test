from django.urls import path
from .views import UserRegisterApi

urlpatterns = [
    path('signup/', UserRegisterApi.as_view())
    
]
