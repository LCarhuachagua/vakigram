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
         'picture': 'https://yt3.googleusercontent.com/ytc/AOPolaQB2hQUpQ27obsfi9NJOvEh4YlH-lcX7X0LZvvzo_s=s176-c-k-c0x00ffffff-no-rj',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://support.hubstaff.com/wp-content/uploads/2019/08/good-pic-300x286.png',
   },
    {
      'title': 'Mont Blance',
      'user': {
         'name': 'Rosellia Vakifahmetoglu',
         'picture': 'https://static.platzi.com/media/avatars/avatars/yazminmanzoolguin1999_603fcb55-b17f-40b7-accd-4a22c5cc91dc.jpeg',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://media.istockphoto.com/id/1300845620/es/vector/icono-de-usuario-plano-aislado-sobre-fondo-blanco-s%C3%ADmbolo-de-usuario-ilustraci%C3%B3n-vectorial.jpg?s=612x612&w=is&k=20&c=zPM_oUwye9se11xNJdiJtq6iCxZ97z7Lpa2GUf1p8GU=',
   },
   {

      'title': 'Mont Blanca',
      'user': {
         'name': 'Rosellie Vakifahmetoglu',
         'picture': 'https://static.platzi.com/media/avatars/avatars/rodrigoariash_19d7a8d7-16f5-4e48-84b4-ce93d90766f3.jpg',
      },
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'photo': 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',

   }
]

def list_posts(request):
   """List existing posts."""
   return render(request, 'feed.html',{
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