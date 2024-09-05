from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Cat, Comment

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'category', 'description', 'photo', 'age', 'color', 'gender']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'margin-bottom:10px; margin-top:50px'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom:10px'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'style': 'margin-bottom:10px', 'rows': '4'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'style': 'margin-bottom:10px'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age', 'style': 'margin-bottom:10px'}),
            'color': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom:10px'}),
            'gender': forms.Select(attrs={'class': 'form-control', }),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'form3Example3'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'form3Example4',
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'form3Example1c'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'form3Example3c',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'form3Example4c'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'form3Example4cd'
    }))

    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'leave your comments here',
                'rows': 4,
                'id': 'textAreaExample',
                'style': 'border: 1px solid black',
            })
        }