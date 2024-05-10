from django.shortcuts import render




def registration(request):
        return render(request, 'web_interface/registration.html')

def login(request):
        return render(request, 'web_interface/login.html')
    
def index(request):
    return render(request, 'web_interface/index.html')


