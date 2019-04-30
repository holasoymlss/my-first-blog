"""myblogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Para cada URL que empiece por admin/ Django encontrará su correspondiente view.
]

from django.urls import include
urlpatterns += [
    #path('blog/', include('blog.urls')), #Todas las URL que empiecen por blog irán a la vista blog.urls y Django buscará más instrucciones allí.
    path('', include('blog.urls')), #utilizo este path para que la URL de inicio de la página no tenga que contener la palabra blog
]
