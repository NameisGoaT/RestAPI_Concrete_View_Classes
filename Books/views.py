from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  

class Studentlistcreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  
class Studentretriveupdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class Studentretrivedestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class Studentretriveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer