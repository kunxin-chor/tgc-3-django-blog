from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # this form will be acting on the Post model
        fields = ('title', 'content', 'pinned')