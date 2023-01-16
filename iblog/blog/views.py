from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

#dummy post

# Create your views here.
def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    #setting new post author(current user)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'about'}) 

