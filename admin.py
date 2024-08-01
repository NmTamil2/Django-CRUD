from django.contrib import admin
from crudApp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        fields = '__all__'

admin.site.register(Student, StudentAdmin)
