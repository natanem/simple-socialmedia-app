from django import forms

from .models import Feed, Comment

class FeedCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'class': 'form-group input-text',
        'placeholder': 'Say something...'

    }))
    class Meta:
        model = Feed
        fields = ['content']

class CommentCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 1,
        'class': 'form-group input-text',
        'placeholder': 'Add a comment...'

    }))
    class Meta:
        model = Comment
        fields = ['content']