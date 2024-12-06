from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, CreatePostForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import PostSerializers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import generics, permissions, status, authentication
from django.urls import reverse_lazy
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


# create a post CRUD operations

class ListPost(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('list_post')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    