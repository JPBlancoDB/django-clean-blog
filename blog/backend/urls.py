from django.urls import path

from .controllers import AuthorsController, PostsController

urlpatterns = [
    path('authors', AuthorsController.get),
    path('authors/<int:id>', AuthorsController.get_by_id),
    path('posts', PostsController.get),
    path('posts/<int:id>', PostsController.get_by_slug),
]
