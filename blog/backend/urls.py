from django.urls import path

from . import api

urlpatterns = [
    path('authors', api.get),
    path('authors/<int:id>', api.get_by_id),
]
