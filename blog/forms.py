from django import forms
from django.core import validators

from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label='Your name',
        required=True,
        max_length=127,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label='Email address',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        # validators=[validators.EmailValidator(message="Invalid Email")]
    )
    comment = forms.CharField(
        label='Your comment',
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Comment
        fields = ('post', 'name', 'email', 'comment')
        widgets = {'post': forms.HiddenInput()}