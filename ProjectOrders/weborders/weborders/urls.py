from django.contrib import admin
from django.urls import path, include

from home.urls import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
]

handler404 = pageNotFound