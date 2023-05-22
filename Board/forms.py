from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category_com',
            'title_post',
            'text_post',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text_post = cleaned_data.get("text_post")
        title_post = cleaned_data.get("title_post")
        if title_post == text_post:
            raise ValidationError("Статья не должно быть идентично названию статьи.")
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post_com',
            'comment',
        ]
