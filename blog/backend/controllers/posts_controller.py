from django.http import JsonResponse

from ..models import Post


class PostsController:

    def get(self):
        posts = Post.get_list()
        return JsonResponse({'data': posts})

    def get_by_slug(self, slug):
        return JsonResponse({'data': Post.get_by_slug(slug)})
