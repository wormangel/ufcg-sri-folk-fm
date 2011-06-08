from django.db import models

# Model

class User(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self')

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
