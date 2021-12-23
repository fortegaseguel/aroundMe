from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import request

import folium
import geocoder
import random

from .models import Post, Comment, Profile, Post, Relationship
from .forms import UserRegisterForm, PostForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def inicio(request):
    posts = Post.objects.all()

    # Caja de comentarios
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('inicio')
    else:
        form = PostForm()

    # Mapa
    m = folium.Map(zoom_start=14)


    for post in posts:
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        
        g = geocoder.ip(ip)
        lat = g.latlng[0]
        long = g.latlng[1]

        folium.Marker(location=[lat, long],popup=post.content ,tooltip=(f'Nuevo post de {post.user}')).add_to(m)

    m= m._repr_html_()


    context = {'posts': posts, 'form': form, 'my_map': m}
    return render(request, 'aroundMe/inicio.html', context)




def details(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    context = {'post': post }
    return render(request, 'aroundMe/details.html', context)



def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.warning(request, f'Los datos ingresados no son válidos. Intente nuevamente')
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'aroundMe/register.html', context)



def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('inicio')



def profile(request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'aroundMe/profile.html', context)



@login_required
def editar(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('inicio')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    
    context = {'u_form': u_form , 'p_form': p_form}
    return render(request, 'aroundMe/editar.html', context)



@login_required
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	return redirect( profile, username)



@login_required
def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user.id)
	rel.delete()
	return redirect(profile, username)



def usuarios(request):
    usuarios = User.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'aroundMe/infousuarios.html', context)

