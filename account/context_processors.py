from account.models import Friend_Request

def get_friend_request(request):
    
    if request.user.is_authenticated:
        friend_requests = Friend_Request.objects.filter(receiver__user=request.user)
    
        return {'friend_requests': friend_requests}
    else:
        return {}