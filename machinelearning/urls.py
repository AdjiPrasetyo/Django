"""machinelearning URL Configuration

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
from django.contrib.auth import views as auth_views
from machinelearning.apps.mlr import views as mlr_views 
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("mlr/", include('machinelearning.apps.mlr.urls')),
    path("", views.index, name="index"),
    # multiple linear regression
    path("dashboard", mlr_views.dashboard, name="dashboard"),
    path("multiple", mlr_views.multiple, name="multiple"),
    path("process", mlr_views.process, name="process"),
    path("update", mlr_views.update, name="update"),
    path("cpo", mlr_views.cpo, name="cpo"),
    path("kpo", mlr_views.kpo, name="kpo"),

    
    
    #path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path(
        "accounts/login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
