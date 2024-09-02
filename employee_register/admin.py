from django.contrib import admin
from .models import Employee, Position

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fullname","position")
    

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Position)

