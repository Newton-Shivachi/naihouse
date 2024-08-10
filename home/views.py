from django.shortcuts import render,get_object_or_404
from .models import Car,Houses
from .forms import SearchForm
from django.db.models import Q

def home(request):
    houses = Houses.objects.filter(forsales=True)[0:6]
    rentals = Houses.objects.filter(forsales=False)[0:6]
    cars = Car.objects.all()[0:6]
    return render(request, 'home/home.html',{
        'houses':houses,
        'rentals':rentals,
        'cars':cars,
    })
    
def HouseForSale(request):
    houses = Houses.objects.filter(forsales=True)
    return render(request, 'home/housesforsales.html', {
        'houses':houses,
    })
    
def HouseForRent(request):
    houses = Houses.objects.filter(forsales=False)
    return render(request, 'home/houseforrent.html', {
        'houses':houses,
    })
    
def Cars(request):
    cars= Car.objects.all()
    return render(request, 'home/cars.html',{
        'cars':cars,
    })
    
def detail(request,pk):
    item = get_object_or_404(Houses, pk=pk)
    return render(request, 'home/detail.html', {
        'item':item,
    })
    
def cardetail(request,pk):
    car = get_object_or_404(Car,pk=pk)
    return render(request, 'home/cardetail.html',{
        'car':car,
    })

def video(request):
    videos = Houses.objects.all()    
    return render(request, 'home/video.html',{
        'videos':videos,
    })
    
def search(request):
    query = request.GET.get('query','')
    items = []
    cars = []
    if query:
        query_words = query.split()
        items_query = Q()
        cars_query = Q()
        for word in query_words:
            items_query &= Q(name__icontains=word) | Q(description__icontains=word) | Q(location__icontains=word)
            cars_query &= Q(name__icontains=word) | Q(description__icontains=word)
        items = Houses.objects.filter(items_query)
        cars = Car.objects.filter(cars_query)
    return render(request,'home/search.html',{
        'query':query,
        'items':items,
        'cars':cars,
    })