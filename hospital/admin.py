from django.contrib import admin
from .models import Doctor,Nurse,Patient,Appointment,PatientDischargeDetails,Room
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class NurseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nurse, NurseAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room,RoomAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
