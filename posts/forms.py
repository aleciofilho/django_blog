from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(max_length=400, widget=forms.Textarea(attrs={"class": "form-control"}))