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

    def can_become_friend(self, user):
        # if I am myself
        if (user.id == self.id):
            return False

        for friend in self.friends.all():
            if (friend.id == user.id):
                return True
        return False

class Tag(models.Model):
    text = models.CharField(max_length=20)
	
class Band(models.Model):
    name = models.CharField(max_length=40)

class UserTagBand(models.Model):
    user = models.ForeignKey(UserProfile)
    tag = models.ForeignKey(Tag)
    band = models.ForeignKey(Band)
