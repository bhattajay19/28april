from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer