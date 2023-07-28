from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'polity', 'science_technology', 'art_culture', 'history', 'maths', 'reasoning', 'ethics', 'geography', 'literature', 'economics'] 