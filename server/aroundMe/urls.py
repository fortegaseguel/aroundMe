"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('details/<int:post_id>/', views.details, name='details'),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='aroundMe/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editar/', views.editar, name='editar'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('usuarios/', views.usuarios, name='usuarios'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
