from django.contrib import admin
from .models import employee
# Register your models here.


class employeeAdmin(admin.ModelAdmin):
    list_display = ('id','EmpName', 'EmpEmail',
                    'EmpDepartment', 'EmpDescription')


admin.site.register(employee, employeeAdmin)
