from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls', namespace='main_app')),
<<<<<<< HEAD
    path('posts/', include('articles.urls', namespace='articles'))
=======
    
    
    path('posts/', include('articles.urls', namespace='articles')),
>>>>>>> 0aadd4ddccf49a4f2c35fec52e86ac2e67c3b9bf
]
