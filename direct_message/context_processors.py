from django.db.models.query_utils import Q
from .models import Conversation, Message

def messages(request):
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(Q(user_one=request.user) | Q(user_two=request.user))
        unsen_messages = []
        for conversation in conversations:
            unsen_messages += list(conversation.messages.filter(user_to=request.user, seen=False))

        return {
            'message_counts' : len(unsen_messages)

        }
    return {'message_counts': 0}