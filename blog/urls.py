from django.urls import URLPattern, path
from .views import BlogListView
app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home")
]