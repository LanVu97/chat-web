from django.apps import apps
import account.views as views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView
# app_name = 'account'
urlpatterns = [
    
    path('login/', include('social_django.urls', namespace='social')),
    path('logout/',LogoutView.as_view(),  name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('user_list/', views.user_list, name='user_list'),
    path('send_friend_request/<int:receiverID>', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:senderID>', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:requestID>', views.decline_friend_request, name='decline_friend_request'),
]