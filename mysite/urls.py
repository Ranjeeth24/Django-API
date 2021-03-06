"""mysite URL Configuration

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
  
"""django_api URL Configuration
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
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'items', views.ItemListViewSet)
router.register(r'modelless', views.ExampleModelLessView, basename='modelless')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', views.login),
    path('logout', views.logout),
    path('check_auth', views.check_auth),
    path('hello/', views.HelloView.as_view(), name='Hello'),
    path('welcome/', views.WelcomeView.as_view(), name='Welcome'),
    path('polls/', views.PollsView.as_view(), name='Polls'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.RegisterView.as_view(), name='Register'),
   
    #    path('post_list', views.post_list, name='post_list'),

]


