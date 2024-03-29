from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

