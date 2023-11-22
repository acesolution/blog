from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.db.models import Count
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, 'index.html')

def content_writing(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Save the form data to the database
            blog_post = form.save(commit=False)
            print(form)
            blog_post.user = request.user

            blog_post.save()
            return redirect('single_blog', blog_id=blog_post.pk)  # Redirect to the blog post detail page
        else:
            print(form.errors)
    else:
        form = BlogPostForm()
    return render(request, 'content-writing.html', {'form': form})

def single_blog(request, blog_id):
    blog_obj = BlogPost.objects.get(id=blog_id)
    tags = blog_obj.tags.all()
     # Annotate each category with the count of related blogs
    categories = Category.objects.annotate(blog_count=Count('blogpost'))
    # Get the current date
    current_date = datetime.now().date()

    # Define a time period for recent blog posts (e.g., 30 days)
    recent_period = current_date - timedelta(days=30)

    # Query for the most recent blog posts created within the last 30 days
    recent_blog_posts = BlogPost.objects.filter(created_date__gte=recent_period).order_by('-created_date')[:10]

    print(recent_blog_posts)

    context = {
        'blog_obj' : blog_obj,
        'tags' : tags,
        'categories' : categories,
        'recent_blog_posts' : recent_blog_posts,
    }
    return render(request, 'politics-details.html', context)

def user_signup(request):
    return render(request, "signup.html")