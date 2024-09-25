from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


# Create your views here.
class StudentInfo(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            s = StudentSerializer(stu)
            return Response(s.data)
        stu = Student.objects.all()
        s= StudentSerializer(stu,many =True)
        return Response(s.data)
    
    def post(self, request, format=None):
        s = StudentSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':'data created successfully..'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format = None):
        if pk:
            stu = Student.objects.get(id=pk)
            s =StudentSerializer(stu,data=request.data)
            if s.is_valid():
                s.save()
            return Response({'msg':'complete data Updated..'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        stu = Student.objects.get(id = pk)
        s =StudentSerializer(stu,request.data,partial = True)
        if s.is_valid():
            s.save()
            return Response({'msg','data is partially updated..'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'data is deleted..'})