# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Welcome to my Django site!")
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html')