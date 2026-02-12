from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Country
from .forms import CountryModifyForm

def home(request):
    # return HttpResponse('Countries')
    return render(request, 'countries/search_form.html')

def all(request):
    countries = Country.objects.all()
    return render(request, 'countries/countries_all.html', context={'countries': countries})

def search(request):
    query = request.GET.get('q')
    if query:
        countries = Country.objects.filter(name__icontains=query)
        return render(request, 'countries/search_results.html', {'countries': countries} )
    return redirect('countries:home')

def modify(request, id):
    try:
        country = Country.objects.get(id=id)
    except:
        return HttpResponseNotFound('Country not found')
    # country = get_object_or_404(Country, id=id)

    if request.method == 'POST':
       form = CountryModifyForm(request.POST, instance=country)
       if form.is_valid():
           form.save()
           return redirect('countries:all')

    form = CountryModifyForm(instance=country)
    return render(request, 'countries/modify_country.html', {'form': form})