<<<<<<< HEAD
from django.urls import path

from . import views

app_name = 'articles'

=======
from django.urls import path 
from .import views 

app_name = 'articles'


>>>>>>> 0aadd4ddccf49a4f2c35fec52e86ac2e67c3b9bf
urlpatterns = [
    path("", views.all_articles_view, name='post_list')
]
