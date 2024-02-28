from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [

        path('', views.index, name='index'),
        path('login/', views.user_login, name='login'),

]
