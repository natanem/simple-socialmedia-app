from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Conversation, Message
from .forms import CreateMessageForm

def message_list_view(request):
    messages = None
    conversations = Conversation.objects.filter(Q(user_one=request.user) | Q(user_two=request.user))
    
    context = {
        'messages' : conversations
    }

    return render(request, 'direct_message/messages.html', context)

def message_detail_view(request, pk):

    conversation = get_object_or_404(Conversation, pk=pk)
    for message in conversation.messages.all():
        if message.user_to == request.user:
            message.seen = True
            message.save()

    if conversation.user_one == request.user:
        user = conversation.user_two
    else:
        user = conversation.user_one


    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_from = request.user
            new_message.user_to = user
            new_message.conversation = conversation
            new_message.save()
            
            return redirect('direct_message:message_detail', conversation.pk)

    else:
        form = CreateMessageForm()

    context = {
        'form' : form,
        'messages' : conversation.messages.all(),
        'conversation' : conversation
    }


    return render(request, 'direct_message/message.html', context)

def message_send_view(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    conversation = None

    if Conversation.objects.filter(Q(user_one=request.user, user_two=user) | Q(user_one=user, user_two=request.user)).exists():
        conversation = Conversation.objects.filter(Q(user_one=request.user, user_two=user) | Q(user_one=user, user_two=request.user))[0]
    else:
        conversation = Conversation.objects.create(user_one=request.user, user_two=user)


    if conversation.user_one == request.user:
        user = conversation.user_two
    else:
        user = conversation.user_one
    

    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_from = request.user
            new_message.user_to = user
            new_message.conversation = conversation
            new_message.save()
            
            return redirect('direct_message:message_detail', conversation.pk)

    else:
        form = CreateMessageForm()

    context = {
        'form' : form,
        'messages' : conversation.messages.all(),
        'conversation' : conversation
    }

    return render(request, 'direct_message/message.html', context)