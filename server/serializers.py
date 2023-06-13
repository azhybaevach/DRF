from rest_framework import serializers
from .models import *


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    disciplines = DisciplineSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'


