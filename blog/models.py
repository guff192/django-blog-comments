from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='article title', max_length=255)
    text = models.TextField(verbose_name='article text', max_length=5000)


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, to_field='id')

    level = models.IntegerField(verbose_name='comment level')
    parent_path = models.CharField(max_length=255, db_index=True)

    text = models.TextField(verbose_name='comment text', max_length=1000)
    time_posted = models.DateTimeField(verbose_name='comment posting time', auto_created=True, db_index=True)

