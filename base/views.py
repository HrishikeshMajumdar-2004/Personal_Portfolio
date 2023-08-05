from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base/home.html')
def about(request):
    return render(request,'base/about.html')
def projects(request):
    return render(request,'base/projects.html')
def education(request):
    return render(request,'base/education.html')
def experience(request):
    return render(request,'base/experience.html')