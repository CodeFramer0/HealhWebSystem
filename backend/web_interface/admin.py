from django.contrib import admin
from web_interface.models import Complaint,Organ


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    pass

@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    pass 