from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login


urlpatterns = [
    path('', views.post_list, name='post_list'), #Asociamos la vista post_list a la URL raíz. Este patrón le dice a Django que views.post_list es el lugar correcto al que ir si alguien entra al sitio web con la dirección http://127.0.0.1:8000/.
	path('<int:pk>/', views.post_texto, name='post_texto'),
	path('info/', views.info, name='info'),
	path('contacto/', views.contacto, name='contacto'),
	path('<slug:the_slug>/', views.post_texto_view, name='post_texto_view'),

]
