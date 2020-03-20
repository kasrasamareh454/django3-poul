"""poul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path , include

from startpage import views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('' , views.start , name='start'),

    #path('authn/', include('authn.urls')),

    path('main/', views.mainpage , name='mainpage'),

    path('quotation/<int:quotation_pk>', views.quotationforedit , name='quotationforedit'),

    path('Qquotation/', views.Qquotation , name='Qquotation'),

    path('main/extra', views.extra , name='extra'),

    path('main/extraC', views.extraC , name='extraC'),

    path('new_s/<int:news_pk>', views.newsnews , name='newsnews'),

    path('createnews/', views.createnews , name='createnews'),

    path('main/scot/' , views.scotpage , name='scotpage'),

    path('authn/signup/' , views.signupuser , name='signupuser'),

    path('authn/logout/' , views.logoutuser , name='logoutuser'),

    path('authn/login/' , views.loginuser , name='loginuser'),

]