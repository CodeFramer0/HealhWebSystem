import logging
from django.shortcuts import render



logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)

def registration(request):
        return render(request, 'web_interface/registration.html')



