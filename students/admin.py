from django.contrib import admin
from students.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname']
	list_filter = ['name']
	search_fields = ['surname', 'name']


admin.register(Student, StudentAdmin)