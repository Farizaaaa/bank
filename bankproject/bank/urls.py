from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from bank import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('x',views.x,name='x'),
    path('f',views.f,name='f'),
]
app_name='bank'
