from django.urls import path

from blog import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)