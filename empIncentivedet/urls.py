from django.urls import path, include
# from .views import *
from .import views

from .views import employeeViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'employee', employeeViewSet)
urlpatterns = [


    #     path('', views.register, name="register"),

    #     path('login', views.login, name="login"),
    #     # path('forms',views.index,name="index"),
    # path('home', views.home, name="home"),
    # path('getdetails', views.getdetails, name="getdetails"),
    path('', include(router.urls)),
    path('user_type', views.user_type, name='user_type'),
    path('register', views.register, name='register'),

    path('loginuser', views.loginuser, name="loginuser"),
    path('main', views.main, name='main'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('getdetails', views.getdetails, name="getdetails"),

    path('index', views.index, name='index'),
    path('deleteuser/<int:id>', views.deleteuser, name='deleteuser'),

    path('updateuser/<int:id>', views.updateuser, name='updateuser'),
    # path('update', views.update, name='update')

]
