"""uspeh URL Configuration

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
from django.urls import path, include
from uspeh.views import BaseView
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout', kwargs={'next_page':'base'}),
    path('design-school/', include('design_school.urls')),
    path('pc-school/', include('pc_school.urls')),
    path('graph-school/', include('graph_school.urls')),
    path('buh-school/', include('buh_school.urls')),
    path('abr-school/', include('abr_school.urls')),
    path('lang-school/', include('lang_school.urls')),
    path('ind-school/', include('ind_school.urls')),
]
