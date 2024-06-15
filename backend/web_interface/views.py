from django.shortcuts import render
from .models import Organ,Complaint



def registration(request):
        return render(request, 'web_interface/registration.html')

def login(request):
        return render(request, 'web_interface/login.html')
    
def index(request):
        organs = Organ.objects.all()
        complaints = Complaint.objects.all()
        return render(request, 'web_interface/index.html',{
                'organs':organs,
                'complaints':complaints
        })


