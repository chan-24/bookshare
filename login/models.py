from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name = 'profile',on_delete=models.CASCADE)
	college = models.CharField(max_length=100,default='')
	email = models.CharField(max_length=100,default='')
	points = models.IntegerField(default=0)



def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)
