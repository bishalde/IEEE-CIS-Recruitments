from django.http import HttpResponse
from django.shortcuts import render,redirect


def homePage(request):
    return render(request,'homePage.html')

def recruitmentForm(request):
    return render(request,'recruitmentForm.html')