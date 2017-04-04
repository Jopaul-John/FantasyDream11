from fantasyapp.models import *
from fantasyapp.urls import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from itertools import chain
from .forms import *


def adminlogin(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        message = "Successful login"
        if user:
            login(request,user)
            return HttpResponseRedirect('/post/')
        else:
            message = "Invalid Credentials"
            return render(request,'admin.html',{'message':message})
    else:
        return render(request,'admin.html',{})

def post(request):
    if request.POST:
        cricform = cricketform(request.POST,request.FILES)
        footform = footballform(request.POST,request.FILES)
        message = "error"
        if cricform.is_valid():
            cricform.updated_on = datetime.now()
            cricform.save()
            message = "succesfully posted"
        elif footform.is_valid():
            footform.updated_on = datetime.now()
            footform.save()
            print("inside football")
            message = "succesfully posted"
        return render(request, 'adminpost.html', {'message': message})

    return render(request,'adminpost.html',{})


def home(request):

    cricmatch = Cricket.objects.all().order_by('-id')[:4]
    footmatch = Football.objects.all().order_by('-id')[:4]
    match = sorted(chain(cricmatch, footmatch),key=lambda instance: instance.on_date,reverse=True)[:4]
    return render(request,'home.html',{'match':match})

def cricket(request):
    tournament = Tournament.objects.filter(is_cricket=True,is_active=True)
    cricket_matches = Cricket.objects.all()

    return render(request, 'cricket.html', {'cricket': cricket_matches,'tournament':tournament})

def cricket_matches(request,id):
    match_info = Cricket.objects.get(id=id)
    print(match_info)

    return render(request,'cricketmatch.html',{'cric':match_info})


def crictournament(request,id):
    mytournament = Tournament.objects.filter(is_cricket=True,is_active=True)
    tournament = Tournament.objects.get(id=id)
    cricket_match = Cricket.objects.filter(tournament=tournament)
    return render(request,'cricket.html',{'cricket': cricket_match,'tournament':mytournament})

def foottournament(request,id):
    mytournament = Tournament.objects.filter(is_football=True,is_active=True)
    tournament = Tournament.objects.get(id=id)
    football_match = Football.objects.filter(tournament=tournament)
    return render(request,'football.html',{'football': football_match,'tournament':mytournament})



def football_match(request,id):
    match_info = Football.objects.get(id=id)
    print(match_info)

    return render(request,'footballmatch.html',{'foot':match_info})

def football(request):
    tournament = Tournament.objects.filter(is_football=True,is_active=True)
    football_matches = Football.objects.all()
    return render(request, 'football.html', {'football': football_matches,'tournament':tournament})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/')