from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hero(request):
    program_context={
        'title':'Home',
        'text':'My Home page for profile',
       

    }
    return render(request, 'hero.html',context=program_context)