


from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.dispatch import receiver 
# from django.db.models.signals import post_save 
# from social_core.backends.google import GoogleOAuth2
# Create your models here.
        
class AccountUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(max_length=200)
    user = models.OneToOneField(AccountUser, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='account' )
    country = models.CharField(blank=True, max_length=200)
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    # @receiver(post_save, sender=AccountUser) 
    # def create_user_profile(sender, instance, created, **kwargs):
    #     print('this is a instance',instance)
    #     if created:
    #         Profile.objects.create(user=instance)
 



class Friend_Request(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE)