# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('home.html')

def user_profile(request, id_user):
    return HttpResponse('This is the user profile page! :D')

def band_profile(request, id_band):
    return HttpResponse('This is the band profile page! :D')

def bands_by_tag(request, id_tag):
    return HttpResponse('This page lists every single band marked with a specific tag! :D')

def recommendations(request):
    return HttpResponse('This is where the FolkRank magic goes! :D')
