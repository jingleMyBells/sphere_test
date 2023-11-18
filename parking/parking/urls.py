from django.contrib import admin
from django.urls import include, path

import vehicles.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(vehicles.urls)),
]
