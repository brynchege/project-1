from django.http import HttpResponse
from django.shortcuts import render




def homepage(request):
    # return HttpResponse("Monster Tech")
    return render(request, "homepage.html")

def about(request):
    # return HttpResponse("We shall run the world")
    return render(request, "about.html")