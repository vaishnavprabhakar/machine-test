from django.urls import path
from .views import (UserRegisterApi,
                    LoginApi,
                    
                    )

urlpatterns = [
    path("signup/", UserRegisterApi.as_view()),
    path("login/", LoginApi.as_view()),
]
