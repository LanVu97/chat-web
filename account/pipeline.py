from .models import Profile
import urllib.request 
from django.conf import settings
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':       
        print(type(user))
        try:
            profile = Profile.objects.get(user__id=user.id)

        except:
            
            profile = Profile.objects.create(user=user)
            url = response['picture']
            local = settings.MEDIA_ROOT + 'account/'

            result = urllib.request.urlretrieve(url, f'{local}avatarUser_{user.id}.jpg')
            link = f'account/avatarUser_{user.id}.jpg'
        
            profile.image = link
            profile.username = user.username
            profile.country = response['locale']
            profile.save()