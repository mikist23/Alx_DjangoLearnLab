from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import PostSerializers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView
from rest_framework import generics, permissions, status, authentication

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'blog/register.html', context=context)

# login user

def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                user = authenticate(username=email, password=password)

                if user:
                    login(request, user)
                    return redirect('profile')
            except User.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginUserForm()
    
    context = {'form':form}
    return render(request, 'blog/login.html', context=context)





# user profile

def profile(request):
    user = User.objects.all()

    return render(request, 'blog/profile.html')


# create a post

class ListPost(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class CreatePost(CreateView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]


class UpdatePost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    