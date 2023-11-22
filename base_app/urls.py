from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('content-genration/', views.content_writing, name='content_writing'),
    path('blog-details/<int:blog_id>/', views.single_blog, name='single_blog'),
    path('sign-up', views.user_signup, name='user_signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)