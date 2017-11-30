from .models import Patients
from rest_framework import serializers


class PatientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patients
        fields = (
            'id',
            'created_at',
            'updated_at',
            'deleted_at',
            'dateInit',
            'nomApe',
            'age',
            'sex',
            'dateNac',
            'address',
            'ocupation',
            'telCel',
            'alergies',
            'operations',
            'diabettes',
            'hipertension',
            'others',
            'treatMedics',
            'state',
        )
