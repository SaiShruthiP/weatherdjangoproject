import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm,Modelcityforms,SearchForm,cityforms
from django.contrib import messages

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bd0900e84b0c3f93ec40e8bfe076fa7b'

    err_msg=''
    message=''
    message_class=''


    if request.method == 'POST':

        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'city does not exist in the world'

                
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'

        else:
            message = 'city added successfuly!'
            message_class = 'is-success'
                 
        
    print(err_msg)
    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'], 
            'icon': r['weather'][0]['icon'],
            
            
        }

        weather_data.append(city_weather)


    context = {
        'weather_data': weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class   
    }

    return render(request,'weather/weather.html',context)


def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')


def citysearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            c = City.objects.filter(name__contains=q)
            form = None
            return render(request,'showtables.html',{'c':c,'form':SearchForm()})
    else:
        form = SearchForm()
        c = City.objects.all()
    return render(request,'showtables.html',{'c':c,'form':form})









