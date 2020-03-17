
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('accounting/', include('accounting.urls')),
    url('drawing/', include('drawingProblems.urls')),
    url('', include('homeService.urls')),
]
