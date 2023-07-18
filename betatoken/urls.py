"""betatoken URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from generatetoken import views

# from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Generate_Token",views.Generate_Token,name="Generate_Token"),
    path("Clean_Tokens",views.Clean_Tokens,name="Clean_Tokens"),
    path("TokenCount",views.TokenCount,name="TokenCount"),
    path("TokenDisplay",views.TokenDisplay,name="TokenDisplay"),
    path("All_Tokens",views.All_Tokens,name="All_Tokens"),

    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    # path('', include('app.urls')),
     path('hello/', views.HelloView.as_view(), name ='hello'),
    path("",include("generatetoken.api.urls"))
     

]
