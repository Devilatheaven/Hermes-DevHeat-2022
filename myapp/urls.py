from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('user',views.user,name='user'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tregister',views.tregister,name='tregister')
]