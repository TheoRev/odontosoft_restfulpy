from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('patients.urls', namespace='patients')),
]

urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]
