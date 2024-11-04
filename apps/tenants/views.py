from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tenant_dashboard_view(request):
    return HttpResponse("Hello, world. You're at the dashboard.")