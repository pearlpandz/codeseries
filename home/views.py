from django.shortcuts import render
from .models import Courses

# Create your views here.
def index(request):
    courses = Courses.objects.all()

    return render(request, 'home.html', {'courses': courses})
