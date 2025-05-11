# blog_app/context_processors.py
from blog_app.models import Category

def categories(request):
    return {'categories': Category.objects.all()}