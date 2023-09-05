"""Post views."""

# Django
from django.shortcuts import HttpResponse

# Utilities
from datetime import datetime

# Create your views here.

posts = [
   {
      'name': 'Mont Blanc',
      'user': 'Roselli Vakifahmetoglu',
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'picture': 'https://support.hubstaff.com/wp-content/uploads/2019/08/good-pic-300x286.png',
   },
    {
      'name': 'Mont Blance',
      'user': 'Rosellia Vakifahmetoglu',
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'picture': 'https://media.istockphoto.com/id/1300845620/es/vector/icono-de-usuario-plano-aislado-sobre-fondo-blanco-s%C3%ADmbolo-de-usuario-ilustraci%C3%B3n-vectorial.jpg?s=612x612&w=is&k=20&c=zPM_oUwye9se11xNJdiJtq6iCxZ97z7Lpa2GUf1p8GU=',
   },
    {
      'name': 'Mont Blanca',
      'user': 'Rosellie Vakifahmetoglu',
      'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
      'picture': 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
   }
]

def list_posts(request):
   """List existing posts."""
   content = []
   for post in posts:
      content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
                     """.format(**post))
   return HttpResponse('<br>'.join(content))