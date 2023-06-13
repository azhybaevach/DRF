from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .models import *
from .serializers import StudentSerializer



class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer
    permission_classes = (IsAuthenticated,)


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer

