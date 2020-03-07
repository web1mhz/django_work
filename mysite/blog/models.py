from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    is_public = models.BooleanField(default=False)
    photo=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

