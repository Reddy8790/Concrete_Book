from django.shortcuts import render 
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentrev(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class StudentUp(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentdel(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentlc(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentru(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentrd(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
class Studentrud(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeriallizer
      
    
      
    
    
    
    