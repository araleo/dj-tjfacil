from django.urls import path

from . import views


app_name = "timekeep"
urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Timekeep
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('<int:task_id>/', views.detalhe, name='detalhe'),
]
