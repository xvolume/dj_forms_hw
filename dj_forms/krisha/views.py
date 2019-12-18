from django.db.models import Q
from django.http import *
from django.shortcuts import render

from .forms import *
from .models import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        userform = RegisterForm(request.POST)

        if userform.is_valid():
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            user = User(username=username, email=email, password=password)
            user.save()
            return render(request, 'krisha/success.html', {'entity': 'User'})
        else:
            return HttpResponse("Invalid data")
    elif request.method == 'GET':
        userform = RegisterForm()
        return render(request, 'krisha/register.html', {'form': userform})

def makepost(request):
    city = Apartment.objects.all()

    if request.method == 'POST':
        postform = MakepostForm(request.POST)
        if postform.is_valid():
            number_of_rooms = postform.cleaned_data['number_of_rooms']
            price = postform.cleaned_data['price']
            year_of_construct = postform.cleaned_data['year_of_construct']
            floor = postform.cleaned_data['floor']
            area = postform.cleaned_data['area']
            city = postform.cleaned_data['city']
            apartment = Apartment(
                number_of_rooms=number_of_rooms,
                price=price,
                year_of_construct=year_of_construct,
                floor=floor,
                area=area,
                city=city
            )
            apartment.save()
            return render(request, 'krisha/success.html', {'entity': 'Post'})
        else:
            return HttpResponse("Invalid data")
    elif request.method == 'GET':
        form = MakepostForm()
        return render(request, 'krisha/makepost.html', {'form': form})

def posts(request):
    posts = Apartment.objects.all()
    query = request.GET.get('query')

    if query:
        if query.isdigit():
            posts = Apartment.objects.filter(Q(id=query)|
                                             Q(price=query))
            return render(request, 'krisha/posts.html', {'posts': posts})
        else:
            city = City.objects.filter(Q(name__icontains=query))
            if city:
                posts = Apartment.objects.filter(Q(city=city[0].pk))
                return render(request, 'krisha/posts.html', {'posts': posts})
            else:
                return render(request, 'krisha/posts.html', {'posts': None})

    return render(request, 'krisha/posts.html', {'posts': posts})

def redirect(request):
    return HttpResponseRedirect('/home')
