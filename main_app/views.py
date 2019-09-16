from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

# Class for our comment form
class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

def home(request):
  return render(request, 'home.html')

def post_index(request):
  post = Post.objects.all().order_by('-created_on')
  return render(request, 'blog/index.html', {'post': post})

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
  return render(request, 'blog/detail.html', { 'post': post , 'form': form, 'comments': comments})

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