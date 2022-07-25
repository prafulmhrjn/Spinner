from django.db import models
from audioop import reverse
# from django.contrib.auth.models import User
# from login.models import Admin

# Create your models here.

class News_post(models.Model):
    news_title = models.CharField(max_length=255, null=True)
    news_description = models.TextField()
    news_snippets = models.CharField(max_length=255)
    news_publisher = models.CharField(max_length=500)
    # admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.news_title

    # def get_absolute_url(self):
    #     return reverse('news')
