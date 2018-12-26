from django.http import JsonResponse

from ..models import Author


class AuthorsController:

    def get(self):
        authors = Author.get_list()
        return JsonResponse({'data': authors})

    def get_by_id(self, id):
        return JsonResponse({'data': Author.get_by_id(id)})
