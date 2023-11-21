from django.contrib import admin
from .models import CustomUser
# Register your models here.


from django.contrib.admin import AdminSite



class DjangoAdinSite(AdminSite):
    enable_nav_sidebar = True
    model = CustomUser


admin.site.register(CustomUser)