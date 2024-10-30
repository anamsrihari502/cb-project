from django.contrib   import admin
from .models import Student

class studentAdmin(admin.ModelAdmin):
    list_display =["first_name","last_name","email","course_name","enrollment_date"]

admin.site.register(Student,studentAdmin)
