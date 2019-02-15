"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path

from urlTrimmer import views,shortcut,admin


template = r"\w\w\w\w"

urlpatterns = [
    path('admin/', admin.index, name="admin"),
    path('', views.index, name="index"),
    re_path('your_url/\w*', views.urlView, name="short_cut"),
    re_path(r"^\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w", shortcut.redirect)

]
