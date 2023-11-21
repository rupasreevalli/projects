from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':510,'b':600}
    return render(request,'conditions.html',d)