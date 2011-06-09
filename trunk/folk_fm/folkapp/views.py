# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from folkapp.models import UserProfile


def index(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def user_profile(request, id_user):
    return HttpResponse('This is the user profile page! :D')

def band_profile(request, id_band):
    return HttpResponse('This is the band profile page! :D')

def bands_by_tag(request, id_tag):
    return HttpResponse('This page lists every single band marked with a specific tag! :D')

def recommendations(request):
    return HttpResponse('This is where the FolkRank magic goes! :D')

@receiver(post_save, sender=User)
def createUserProfile(sender, **kwargs):
    if (kwargs['created'] == True):
        profile = UserProfile(name=kwargs['instance'].username, user=kwargs['instance'])
        profile.save()
        profile.id

def populate_test_db(request):
    lucas = User(username='lucas')
    lucas.set_password('123')
    lucas.save()
    lucas.id
    return HttpResponse('Ok!')
