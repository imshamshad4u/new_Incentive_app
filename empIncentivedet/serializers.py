# from django.contrib.auth.models import employee
from .models import employee
from rest_framework import routers, serializers, viewsets


class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"
