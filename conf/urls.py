from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quechat.urls')),
    path('auth/',include('users.urls')),
]
