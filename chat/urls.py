from django.apps import apps
import chat.views as views

from django.urls import  path


urlpatterns = [

    path('', views.chat_view, name='chat'),
    path('messages/<int:sender>/<int:receiver>', views.message_view, name='message-detail'),
    path('get_message_new/<int:sender>/<int:receiver>', views.get_message_new, name='get_message_new'),
    path('send/', views.send_view, name='send'),
    
]