from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def education(request):
    return render(request,'education.html')
def schools(request):
    return render(request,'schools.html')
def college(request):
    return render(request,'college.html')
def university(request):
    return render(request,'university.html')