from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.contrib.auth.forms import UserCreationForm


def welcome(request):
    return render(request, 'PracticeEnglish/welcome.html' )

def example_learning(request):
    context ={
        'examples' : example.objects.all()
    }
    return render(request, 'PracticeEnglish/example.html', context)


def verbs_court(request):
    if request.method == "POST":
        form = request.POST
        verb_court.objects.create(verb = form["verb"],meaning = form["meaning"])

    context ={
        'verbs_court' : verb_court.objects.all()
    }
    return render(request, 'PracticeEnglish/verbs_court.html', context)
def verbs_restaurant(request):
    if request.method == "POST":
        form = request.POST
        verb_restaurant.objects.create(verb = form["verb"],meaning = form["meaning"])

    context ={
        'verbs_restaurant' : verb_restaurant.objects.all()
    }
    return render(request, 'PracticeEnglish/verbs_restaurant.html', context)
def verbs_airport(request):
    if request.method == "POST":
        form = request.POST
        verb_airport.objects.create(verb = form["verb"],meaning = form["meaning"])

    context ={
        'verbs_airport' : verb_airport.objects.all()
    }
    return render(request, 'PracticeEnglish/verbs_airport.html', context)
def verbs_hotel(request):
    if request.method == "POST":
        form = request.POST
        verb_hotel.objects.create(verb = form["verb"],meaning = form["meaning"])

    context ={
        'verbs_hotel' : verb_hotel.objects.all()
    }
    return render(request, 'PracticeEnglish/verbs_hotel.html', context)

def phrases_say(request):
    if request.method == "POST":
        form = request.POST
        phrase_say.objects.create(phrase = form["phrase"],meaning = form["meaning"])

    context ={
        'phrases_say' : phrase_say.objects.all()
    }
    return render(request, 'PracticeEnglish/phrases_say.html', context)
def phrases_off(request):
    if request.method == "POST":
        form = request.POST
        phrase_off.objects.create(phrase = form["phrase"],meaning = form["meaning"])

    context ={
        'phrases_off' : phrase_off.objects.all()
    }
    return render(request, 'PracticeEnglish/phrases_off.html', context)
def phrases_afraid(request):
    if request.method == "POST":
        form = request.POST
        phrase_afraid.objects.create(phrase = form["phrase"],meaning = form["meaning"])

    context ={
        'phrases_afraid' : phrase_afraid.objects.all()
    }
    return render(request, 'PracticeEnglish/phrases_afraid.html', context)

def new_things_me_too(request):
    if request.method == "POST":
        form = request.POST
        new_thing_me_too.objects.create(new = form["new"], example = form["example"])

    context ={
        'new_things_me_too' : new_thing_me_too.objects.all()
    }
    return render(request, 'PracticeEnglish/new_things_me_too.html', context)
def new_things_ithink(request):
    if request.method == "POST":
        form = request.POST
        new_thing_ithink.objects.create(new = form["new"], example = form["example"])

    context ={
        'new_things_ithink' : new_thing_ithink.objects.all()
    }
    return render(request, 'PracticeEnglish/new_things_ithink.html', context)
def new_things_very(request):
    if request.method == "POST":
        form = request.POST
        new_thing_very.objects.create(new = form["new"], example = form["example"])

    context ={
        'new_things_very' : new_thing_very.objects.all()
    }
    return render(request, 'PracticeEnglish/new_things_very.html', context)

def choose_new_thing_group(request):
    return render(request, 'PracticeEnglish/choose_new_thing_group.html')
def choose_verb_group(request):
    return render(request, 'PracticeEnglish/choose_verb_group.html')
def choose_phrase_group(request):
    return render(request, 'PracticeEnglish/choose_phrase_group.html')
