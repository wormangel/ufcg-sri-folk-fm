from django.db import models
from django.contrib.auth.models import User

# Model

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self')
    user = models.OneToOneField(User)

    def tag(self, band, tagText):
        pass

    def addFriend(self, user):
        pass

class Tag(models.Model):
    text = models.CharField(max_length=20)
	
class Band(models.Model):
    name = models.CharField(max_length=40)

class UserTagBand(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    band = models.ForeignKey(Band)
