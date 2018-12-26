from django.urls import path

from .controllers import AuthorsController

urlpatterns = [
    path('authors', AuthorsController.get),
    path('authors/<int:id>', AuthorsController.get_by_id),
]
