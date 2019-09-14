from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Comment

# This is our Create Post view. We create new posts passing in the fields from the model.
class PostCreate(CreateView):
  model = Post
  fields = '__all__'
  success_url = '/'

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = '/'

def home(request):
  return render(request, 'home.html')

def post_index(request):
  post = Post.objects.all()
  return render(request, 'blog/index.html', {'post': post})

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'blog/detail.html', { 'post': post })

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