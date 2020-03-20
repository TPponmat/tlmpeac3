from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tlmapi/', include('tlmapi.urls')),
    path('admin/', admin.site.urls),
]