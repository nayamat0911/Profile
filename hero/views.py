from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hero(request):
    program_context={
        'title':'Home page',
        'text':'My Home page for profile',
       

    }
    return render(request, 'basic.html',context=program_context)