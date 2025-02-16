"""mysite URL Configuration

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
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.FTP_session_view.index), ## INDEX PAGE
    path('visualise', views.FTP_session_view.visual), ## PLOTS PAGE
        path('ftp_login', views.FTP_session_view.ftp_login), ## FTP PAGE
        path('plots/', views.FTP_session_view.make_plots), ## plots PAGE
        path('visualising', views.FTP_session_view.visualising), ## PLOTS PAGE
        path('visualising2', views.FTP_session_view.visualising2), ## PLOTS PAGE

    #path('results', views.FTP_session_view.results), ## INDEX PAGE

    ]
