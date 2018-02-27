"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include, path


# from '../client/components/Home.vue' import Home



# from '../client/components/PersonalPage.vue' import PersonalPage

from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/current-user', views.UserView.as_view(), name='current-user'),
    path('', views.index),
    path('home/', views.index, name='home'),
    # url(r'^home/$', views.index, name='home'),
    url(r'^blog/$', views.index, name='blog'),
    url(r'^personal-page/$', views.index, name='personalPage'),
    # path('home', views.index, name='home'),
    # path('/blog', views.VueRouter, name='Blog'),
    # path('personal-page/', PersonalPage.as_view(), name='PersonalPage'),
    # path('blog/', views.blog, name='blog'),

]