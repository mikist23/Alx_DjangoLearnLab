from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, CreatePostForm, CommentForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import generics, permissions, status, authentication
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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
                    return redirect('list_post')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Retrieve the Post instance
        comment = Comment(
            post=post,
            author=request.user,
            content=request.POST.get('content')
        )
        comment.save()
        return redirect(post.get_absolute_url())  # Redirect to the post detail page


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'
    success_url = '/posts/'

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
    

# Comment CRUD operations
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment 

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    def test_func(self):
        return self.request.user == self.get_object().author
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    def test_func(self):
        return self.request.user == self.get_object().author
    

# views for search post

# Search Posts View
def search_posts(request):
    query = request.GET.get('q', '')  # Default to an empty string if no query is provided
    posts = Post.objects.all()  # Start with all posts
    if query:
        # Explicit use of Post.objects.filter
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()  # Avoid duplicate results
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})




class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Retrieve the tag based on the slug from the URL
        tag_name = self.kwargs.get('tag_name')
        tag = get_object_or_404(Tag, name=tag_name)
        # Filter posts associated with the tag
        return Post.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        # Pass the tag to the template for display
        context = super().get_context_data(**kwargs)
        tag_name = self.kwargs.get('tag_name')
        context['tag'] = get_object_or_404(Tag, name=tag_name)
        return context