from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.db.models import Q

from chat.models import Message
# Create your views here.
@login_required(login_url='/')
def chat_view(request):
    context = {}
    list_friends = Profile.objects.filter(friends__user=request.user)
    context['list_friends'] = list_friends
    return render(request, "chat/chat.html", context)

@login_required(login_url='/')
def message_view(request, sender, receiver): 
    # if request.method == "GET":
    context = {}
    list_friends = Profile.objects.filter(friends__user=request.user)
    # Receiver context user object for using in template
    receiver = Profile.objects.get(user__id=receiver)
    # Return context with message objects where users are either sender or receiver.
    messages = Message.objects.filter(Q(sender_id=sender, receiver_id=receiver) | Q(sender_id=receiver, receiver_id=sender))
    messages.update(seen=True)

    context['list_friends'] = list_friends
    context['receiver'] = receiver
    context['messages'] = messages
    
    return render(request, "chat/messages.html",context) 

@login_required(login_url='/')
def get_message_new(request, sender, receiver): 
    receiver = Profile.objects.get(user__id=receiver)
    messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, seen=False)
    # print(messages)    
    context = {
        "messages":list(messages.values())
    }
     
    messages.update(seen=True)
    
    return JsonResponse(context)

@login_required(login_url='/')
def send_view(request):
    message = request.POST['message']
    sender_id = request.POST['sender']
    sender = Profile.objects.get(user__id = sender_id)
    receiver_id = request.POST['receiver']
    receiver = Profile.objects.get(user__id = receiver_id)

    new_message = Message.objects.create(sender=sender, receiver=receiver, message=message)
    # print(new_message)
    message = {
            "message": new_message.message,
        }
    return JsonResponse({"new_message ":message})