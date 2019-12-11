from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .forms import PostForm
from .models import Post

def all_posts(request):
   posts = Post.objects.all().values()
   return JsonResponse({
       'data':list(posts)
   })
   
def update_post(request, id):
     if request.method == 'POST':
         model = get_object_or_404(Post, pk=id)
         form = PostForm(request.body, instance=model)
         if form.is_valid():
             form.save()
         else:
             return form.errors.as_json()
     else:
             return JsonResponse({
                 'error': "Invalid method"
             })

