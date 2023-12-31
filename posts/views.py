"""Post views."""

# Django
from django.contrib.auth.decorators import login_required
#from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
#from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# Utilities
from datetime import datetime

# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
   """Return all published posts."""
   template_name = 'posts/feed.html'
   model = Post
   ordering = ('-created',)
   paginate_by = 30
   context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
   """Return post detail."""

   template_name = 'posts/detail.html'
   queryset = Post.objects.all()
   context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
   """Create new post view."""
   template_name = 'posts/new.html'
   form_class = PostForm
   success_url = reverse_lazy('feed')

   def get_context_data(self, **kwargs):
      """Add user and profile to context."""
      context = super().get_context_data(**kwargs)
      context['user'] = self.request.user
      context['profile'] = self.request.user.profile
      return context  

#def create_post(request):
#   """Create new post view."""
#   if request.method == 'POST':
#      form = PostForm(request.POST, request.FILES)
#      if form.is_valid():
#         form.save()
#         return redirect('feed')
#   else:
#      form = PostForm()

#   return render(
#      request =request,
#      template_name='posts/new.html',
#      context={
#         'form': form,
#         'user': request.user,
#         'profile': request.user.profile
#      }
#   )

#def list_posts(request):
#   """List existing posts."""
#   posts = Post.objects.all().order_by('-created')
#   return render(request, 'posts/feed.html',{
#      'posts': posts #esta variable posts es el diccionario definido en linea 12
#      })

#@login_required
   
   #content = []
   #for post in posts:
   #   content.append("""
   #    <p><strong>{name}</strong></p>
   #     <p><small>{user} - <i>{timestamp}</i></small></p>
   #    <figure><img src="{picture}"/></figure>
   #                 """.format(**post))
   #return HttpResponse('<br>'.join(content))

