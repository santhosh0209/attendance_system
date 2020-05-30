from django.contrib import admin
from .models import Faculty,Student,Subject,SelectedSubject,AttendanceRecord



class EventAdmin(admin.ModelAdmin):
    model = Faculty
    list_display = ['user']





admin.site.register(Faculty,  EventAdmin)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SelectedSubject)
admin.site.register(AttendanceRecord)
#pass=admin, adminadmin
