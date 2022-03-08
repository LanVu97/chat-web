
from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import UpdateProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/')
def profile_view(request):

    context = {}
    if request.method == 'POST':
        profile = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid():
            profile.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        profile = UpdateProfileForm(instance=request.user.profile)
        context['profile'] = profile
    return render(request, "account/profile.html", context)