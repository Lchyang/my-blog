from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 一个分类多个文章， 一对多
    category = models.ForeignKey(Category)
    # 一个文章多个标签， 一个标签多个文章，多对多。
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)
    #views 记录阅读量
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    # 自动生成post的URL
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


