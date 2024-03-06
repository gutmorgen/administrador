from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [

        path('', views.index, name='index'),
        path('panel_socio',views.panel_socio, name='panel_socio'),
        path('', include('django.contrib.auth.urls')),

]
