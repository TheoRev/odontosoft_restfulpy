from rest_framework import generics
from .models import Patients
from .serializers import PatientsSerializer
from django.shortcuts import get_object_or_404

class PatientsList(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj=get_object_or_404(
            queryset,
            pk=self.kwargs('pk'),
        )
        return obj
