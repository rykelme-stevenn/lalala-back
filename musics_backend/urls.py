from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('musics_backend.api.urls')),  # aponte para o urls.py do app "api"
]
#     