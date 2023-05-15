from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    # jwt auth
    path('login/', views.TokenObtainPairView.as_view(), name='login'),
    # path('auth/', include('djoser.urls.jwt')),
    path('stocksinfo/', include('stocksinfo.urls')),
]
