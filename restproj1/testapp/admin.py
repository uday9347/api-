from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empid','empname','empsal']


admin.site.register(Employee,EmployeeAdmin)