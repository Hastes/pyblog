from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(verbose_name=('Заголовок'),max_length=200,name='title')
    text = models.TextField(verbose_name=('Текст'))
    created_date = models.DateTimeField(verbose_name=('Дата создания'),
            default=timezone.now)
    published_date = models.DateTimeField(verbose_name=('Дата публикации'),
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date',]


class Comment(models.Model):
    comment_author = models.CharField(max_length=200,verbose_name="Ваше имя")
    comment_text = models.TextField(verbose_name="Текст")
    comment_created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    class Meta:
        ordering = ['-comment_created_date']