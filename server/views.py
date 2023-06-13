from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import StudentSerializer



class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer

