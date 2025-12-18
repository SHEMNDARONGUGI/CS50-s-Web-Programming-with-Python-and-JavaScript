from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def index(request):
    return render(request, 'LMS/index.html')

def contact(request):
    return render(request, 'LMS/contact.html')

def about(request):
    return render(request, 'LMS/about.html')

def course_details(request):
    return render(request, 'LMS/course-details.html')

def courses(request):
    return render(request, 'LMS/courses.html')

def events(request):
    return render(request, 'LMS/events.html')

def pricing(request):
    return render(request, 'LMS/pricing.html')

def greet(request, name):
    return HttpResponse(f'Hello, { name }')
    