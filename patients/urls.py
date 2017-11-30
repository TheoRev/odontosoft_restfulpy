from django.conf.urls import url
from patients.views import *


urlpatterns = [
    url(r'^patients/$', PatientsList.as_view(), name='patients')
]
