# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("Hello, world. You're at the myProject home page.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Hello, world. You're at the myProject about page.")
    return render(request, 'about.html')