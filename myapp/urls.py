from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('contactus',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('user',views.user,name='user'),
    path('logout',views.logout,name='logout')
]