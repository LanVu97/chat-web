
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/')
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {}
    if request.method == 'POST':
        pass
    else:
        context['profile'] = profile
    return render(request, "account/profile.html", context)