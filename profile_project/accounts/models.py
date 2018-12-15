from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	birth_date = models.DateField(null=True)
	bio = models.TextField(default='')
	avatar = models.ImageField(upload_to='media/', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()