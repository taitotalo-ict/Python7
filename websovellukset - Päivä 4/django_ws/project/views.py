from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
# from django.views.generic import ListView

# def hello(request):
#     return HttpResponse('Hello world')

class HelloView(View):
    def get(self, request, name):
        return HttpResponse(f'Hello {name}. {reverse('hello', args=['christian'])}')

def calendar(request, year):
    return HttpResponse(f'Calendar from year {year}')

def isocalendar(request, isodate):
    return HttpResponse(f'Calendar from year {isodate.year}')

def homepage(request):
    return render(request, 'homepage.html', context={'title': 'Homepage'})
    query_params = request.GET
    active = request.GET.get('active')
    return HttpResponse(f'Homepage: {list(query_params.items())}<br>Active: {active}')

def redirect_view(request):
    name = request.GET.get('name', 'Christian')
    return HttpResponseRedirect(reverse('hello', args=[name]))
    return redirect('hello', name=name)

def tag_view(request):
    return render(request, 'tags.html', context={'tags': request.GET})