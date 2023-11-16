"""
URL configuration for recipe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include
from django.conf import settings # from project level settings.py
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('recipes.urls')),
   path('', include('users.urls')),      
   path('', include('ingredients.urls'))       
]

# url patterns is similar to router endpoints

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# appending to urlpatterns array with static elements of image urls and root

