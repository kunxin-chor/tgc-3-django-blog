"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import index, about_us, create_post, update_post, delete_post, update_post_ajax
from posts.api import all_posts
import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', index),
    path('profile', about_us),
    path('add_post', create_post),
    path('edit_post/<post_id>', update_post),
    path('edit_post_ajax/<post_id>', update_post_ajax),
    path('delete_post/<post_id>', delete_post),
    path('api/posts', all_posts),
    path('api/update_post/<id>', posts.api.update_post)
]
