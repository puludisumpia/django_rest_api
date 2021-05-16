from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/posts/", blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
