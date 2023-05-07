"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from myapp.views import first_page,index,detail,index_login,index_register
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/',first_page),
    path('index/', index,name='index'),
    re_path(r'^detail/(?P<page_num>\d+)$',detail,name='detail'),
    path('login/',index_login,name='login'),
    path('upload/',index),
    path('register',index_register,name='register'),
    path('logout',logout_then_login,{'login_url':'/login'},name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
