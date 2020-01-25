from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100) #Limited Text
    content = models.TextField() #Unlimited Text
    date_posted = models.DateTimeField(default=timezone.now) #auto_now_date=True doesnot update the post date.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete will delete the post of the user when the user will be deleted

    def __str__(self):
        return self.title #to see the post title in shell command

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})