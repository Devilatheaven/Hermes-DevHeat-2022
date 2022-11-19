from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('user',views.user,name='user'),
    path('logout',views.logout,name='logout'),
    path('material',views.material,name='material'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tregister',views.tregister,name='tregister'),
    path('tlogin',views.tlogin,name='tlogin'),
    path('student_quiz',views.student_quiz,name='student_quiz'),
    path('quiz_questions',views.quiz_questions,name='quiz_questions')
]