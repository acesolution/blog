# forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'read_time', 'post_image', 'tags', 'category',  'content']


    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'read_time': forms.NumberInput(attrs={'class': 'form-control'}),
        'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        
    }