from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "kategorie"
        verbose_name = "kategorie"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "posty"
        verbose_name = "post"

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "komentarze"
        verbose_name = "komentarze"

    def __str__(self):
        return f"Komentarz użytkownika {self.author} w poście: '{self.post}'"