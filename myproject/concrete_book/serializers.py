from rest_framework import serializers
from .models import *


class StudentSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
