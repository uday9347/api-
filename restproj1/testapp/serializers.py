from rest_framework import serializers 
from testapp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    empname=serializers.CharField()
    empsal=serializers.FloatField()

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self,inst,validated_data):
        inst.empid=validated_data.get('empno',inst.empid)
        inst.empname=validated_data.get('empname',inst.empname)
        inst.empsal=validated_data.get('empsal',inst.empsal)
        print(inst.empname)
        inst.save()
    
        return inst

       