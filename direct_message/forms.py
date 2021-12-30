from django import forms
from .models import Conversation, Message


class CreateMessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'class': 'form-group input-text',
        'placeholder': 'Say something...'

    }))
    class Meta:
        model = Message
        fields = ['content']


