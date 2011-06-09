# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from folkapp.models import *


def index(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def user_list(request):
    users = UserProfile.objects.all()
    return render_to_response('user_list.html', {'users': users}, context_instance=RequestContext(request))

@login_required
def user_profile(request, id_user):
    user_profile = get_object_or_404(UserProfile, pk=id_user)
    can_add = request.user.get_profile().can_become_friend(user_profile)
    return render_to_response('user_profile.html', {'user_profile': user_profile, 'can_add': can_add}, context_instance=RequestContext(request))

@login_required
def band_list(request):
    bands = Band.objects.all()
    return render_to_response('band_list.html', {'bands': bands}, context_instance=RequestContext(request))

@login_required
def band_profile(request, id_band):
    band = get_object_or_404(Band, pk=id_band)
    return render_to_response('band_profile.html', {'band': band}, context_instance=RequestContext(request))

@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render_to_response('tag_list.html', {'tags': tags}, context_instance=RequestContext(request))

@login_required
def bands_by_tag(request, id_tag):
    chosen_tag = Tag.objects.get(id=id_tag)
    utbs = UserTagBand.objects.filter(tag=chosen_tag)
    
    bands = [utb.band for utb in utbs]

    return render_to_response('bands_by_tag.html', {'bands': bands, 'tag': chosen_tag}, context_instance=RequestContext(request))

@login_required
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
    vitor = User(username='vitor')
    vitor.set_password('123')
    vitor.save()
    for i in range(1,11):
        banda = Band(name='banda' + str(i))
        banda.save()
    tag = Tag(text='Impar')
    tag.save()
    for i in range(1,11,2):
        banda = Band.objects.get(id=i)
        utb = UserTagBand(user=lucas.get_profile(), tag=tag, band=banda)
        utb.save()
    return HttpResponse('Ok!')
