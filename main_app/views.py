from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .models import Comment

# This is our Create Post view. We create new posts passing in the fields from the model.
class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'categories', 'company', 'company_office_city', 'body']
  success_url = '/post'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'categories', 'company', 'company_office_city', 'body']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post'

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']
    success_url = f'/post'

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/post'

class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        self.results = Post.objects.filter(title__icontains=query)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)
        
# Class for our comment form
class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            'cols': 1, 'rows': 5
        })
    )

def home(request):
  return render(request, 'home.html')

def post_index(request):
  post = Post.objects.all().order_by('-created_on')
  return render(request, 'blog/index.html', {'post': post})

# PLEASE TELL ME IF YOU ARE TOUCHING THE POST_DETAIL VIEWS FUNCTION
@login_required
def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  currentUser = request.user
  user_id = currentUser.id
  # Post views counter not working properly
  post.blog_views=post.blog_views + 1
  post.save()
  form = CommentForm()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = Comment(
        body=form.cleaned_data["body"],
        post=post,
        user_id=user_id
      )
      comment.save()
      form = CommentForm()
      
  comments = Comment.objects.filter(post=post).order_by('-created_on')
  context = {
    "post": post,
    "comments": comments,
    "form": form,
  }
  user_voted = post.votes.exists(request.user.id)
  return render(request, 'blog/detail.html', { 'post': post , 'form': form, 'comments': comments, 'user_voted': user_voted})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      # This is the route that will redirect after a succesful sign up.
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  

# The upvote view. After voting a post up, redirect back to the previous url page
def upVote(request, post_id):
  post = Post.objects.get(id=post_id)

  if post.votes.exists(request.user.id):
    downVote(request, post_id)
  else:
    post.votes.up(request.user.id)
  return HttpResponseRedirect(f'/post/{post_id}')

# The downvote view. After voting a post down, redirect back to the previous url page
def downVote(request, post_id):
  post = Post.objects.get(id=post_id)
  post.votes.down(request.user.id)
  return HttpResponseRedirect(f'/post/{post_id}')

def vent_index(request):
  posts = Post.objects.filter(categories='V').order_by('-created_on')
  return render(request, 'category/vent.html', {'posts': posts})

def info_index(request):
  posts = Post.objects.filter(categories='I').order_by('-created_on')
  return render(request, 'category/info.html', {'posts': posts})

def help_index(request):
  posts = Post.objects.filter(categories='H').order_by('-created_on')
  return render(request, 'category/info.html', {'posts': posts})