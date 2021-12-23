from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Post, Relationship


#Registro de Usuarios
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


# Comentarios

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs= {
        'class': 'form-control w-100',
        'id': 'contentsBox', 
        'rows' : '3',
        'placeholder': '¿En que estas pensando?'
    }))

    class Meta:
        model = Post
        fields = ['content']


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']



# Editar Usuario y Perfil de Usuario
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio']

