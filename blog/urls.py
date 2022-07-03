from django.urls import URLPattern, path
from .views import BlogListView, BlogCreateView
app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create")
]