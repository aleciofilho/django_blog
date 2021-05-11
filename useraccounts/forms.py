from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Profile

# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password'
#         ]

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         qs = User.objects.filter(username__iexact=username)
#         if not qs.exists():
#             raise forms.ValidationError("Invalid username.")
#         return username
    
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    #     return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid username.")
        return username
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

class RegisterForm(forms.Form):
    error_css_class = 'is-invalid'
    # required_css_class = ''

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

# class RegisterForm(forms.ModelForm):
#     password2 = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "password"
#         ]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username has already been taken.", code="username_taken")
        if len(username) < 4:
            raise forms.ValidationError("This username is too short.", code="username_short")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.", code="email_taken")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two passwords didn't match.", code="password_mismatch")
        return password2

    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     username_qs = User.objects.filter(username__iexact=username)
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     email = self.cleaned_data.get("email")
    #     email_qs = User.objects.filter(email__iexact=email)
    #     if username_qs.exists():
    #         raise forms.ValidationError("This is not a valid username.", code="invalid_username")
    #     if email_qs.exists():
    #         raise forms.ValidationError("This is not a valid email.", code="invalid_email")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("The two passwords didn't match.", code="password_mismatch")
    #     return self.cleaned_data

class UserUpdateModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserUpdateModelForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        user = self.request.user
        if qs.exists() and not user.username == username:
            raise forms.ValidationError("This username has already been taken.", code="username_taken")
        if len(username) < 4:
            raise forms.ValidationError("This username is too short.", code="username_short")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        user = self.request.user
        if qs.exists() and not user.email == email:
            raise forms.ValidationError("This email is already in use.", code="email_taken")
        return email

class ProfileUpdateModelForm(forms.ModelForm):
    bio = forms.CharField(max_length=400, widget=forms.Textarea(attrs={"class":"form-control"}))
    # profile_pic = forms.ImageField(widget=forms.i(attrs={"class":"form-control"}))

    class Meta:
        model = Profile

        fields = [
            "bio",
            "profile_pic"
        ]