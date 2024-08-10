from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
# Create your views here.
class EmployeeView(APIView):
    def get(self,request,id=None):
        if id is None:
            eobj=Employee.objects.all()

            pdict=EmployeeSerializer(eobj,many=True)
            
            return Response(pdict.data )
        eobj=Employee.objects.get(id=id)
        pdict=EmployeeSerializer(eobj)
      
        return Response(pdict.data )

        
    def post(self,request,id):
        serializer=EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        data={'msg':'the resouce is created'}
        return Response(data)
    def put(self,request,id):
        inst=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(inst,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
           
            obj=serializer.save()
            print(obj.empname)
        data={'msg':'the resouce is created'}
        return Response(data)
    def patch(self,request,id):
        inst=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(inst,data=request.data,partial=True)
        if serializer.is_valid():
            print(serializer.validated_data)
           
            obj=serializer.save()
           
        data={'msg':'the resouce is created'}
        return Response(data)
    def delete(self,request,id):
        inst=Employee.objects.get(id=id)
        inst.delete()
        data={'msg':'the resouce is deleted successfully'}

        return Response(data)
    

