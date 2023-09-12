"""Post views."""

# Django
#from django.shortcuts import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime

# Create your views here.

posts = [
   {
      'title': 'Mont Blanc',
      'user': {
         'name': 'Roselli Vakifahmetoglu',
         'picture': 'https://picsum.photos/60/60/?image=1027',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://picsum.photos/800/600?image=1036',
   },
    {
      'title': 'Mont Blance',
      'user': {
         'name': 'Rosellia Vakifahmetoglu',
         'picture': 'https://picsum.photos/60/60/?image=1005',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://picsum.photos/800/800/?image=903',
   },
   {

      'title': 'Mont Blanca',
      'user': {
         'name': 'Rosellie Vakifahmetoglu',
         'picture': 'https://picsum.photos/60/60/?image=883',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://picsum.photos/500/700/?image=1076',

   }
]

def list_posts(request):
   """List existing posts."""
   return render(request, 'posts/feed.html',{
      'posts': posts #esta variable posts es el diccionario definido en linea 12
      })
   
   #content = []
   #for post in posts:
   #   content.append("""
   #    <p><strong>{name}</strong></p>
   #     <p><small>{user} - <i>{timestamp}</i></small></p>
   #    <figure><img src="{picture}"/></figure>
   #                 """.format(**post))
   #return HttpResponse('<br>'.join(content))