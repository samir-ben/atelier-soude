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

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path
from blog import views
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/current-user', views.UserView.as_view(), name='current-user'),
    url(r'^blog/', include('blog.urls')),
    url(r'^event/$', views.index, name='event'),
    path('', views.index),
    path('home/', views.index, name='home'),
    url(r'^personal-page/$', views.index, name='personalPage'),
    url(r'^contact/$', views.index, name='contact'),
    url(r'^contact/[a-zA-Z1-9_]{0,2}|10', views.index, name='showContact'),


]
