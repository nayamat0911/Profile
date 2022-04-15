from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def About(request):
    about_context={
        'title':'about',
        'text':'My About page for profile',
       

    }
    return render(request, 'about.html',context=about_context)