from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard_view(request):
    return render(request, 'core/dashboard.html')