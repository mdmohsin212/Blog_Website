from django import forms
from post.models import Post

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']