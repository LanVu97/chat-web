import account.views as views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', include('social_django.urls', namespace='social')),
    path('logout/',LogoutView.as_view(),  name='logout'),
    path('profile/', views.profile_view, name='profile'),
]