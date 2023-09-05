"""Posts application module"""
from django.apps import AppConfig

"""This is the app config file"""
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Posts'
