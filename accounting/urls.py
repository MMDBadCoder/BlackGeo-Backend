
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('forgot/', include('accounting.forgot.urls')),
    url('sign', include('accounting.sign.urls'))
]
