from django.http import HttpResponse
from django.views import View
# from django.views.generic import ListView

# def hello(request):
#     return HttpResponse('Hello world')

class HelloView(View):
    def get(self, request, name):
        return HttpResponse(f'Hello {name}')

def calendar(request, year):
    return HttpResponse(f'Calendar from year {year}')

def isocalendar(request, isodate):
    return HttpResponse(f'Calendar from year {isodate.year}')

def homepage(request):
    return HttpResponse('Homepage')