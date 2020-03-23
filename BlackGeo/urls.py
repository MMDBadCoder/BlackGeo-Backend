from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('accounting/', include('accounting.urls')),
    url('drawing-solution/', include('drawingSolutions.urls')),
    url('drawing/', include('drawingProblems.urls', 'drawing')),
    url('set/', include('setManager.urls', namespace='sets')),
    url('home/', include('homeService.urls')),
]
