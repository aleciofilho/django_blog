from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(max_length=400, widget=forms.Textarea(attrs={"class": "form-control"}))
    
    class Meta:
        model = Post
        fields = [
            "title",
            "content"
        ]