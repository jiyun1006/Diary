from django.db import models
from django_girls.models import TimeStampedModel


class Article(TimeStampedModel):
    title=models.CharField(max_length=100, verbose_name= '제목')
    content = models.TextField(verbose_name='내용')


