from django.db import models

class Question(models.Model):
    # ...
    question_text = models.CharField(max_length=200)
    question_logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.question_text
    # ...

class Choice(models.Model):
    # ...
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
    ...

from django.contrib.auth.models import User
from django.db import models

class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class Type(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    result = models.CharField(max_length=100)
    nick = models.CharField(max_length=100, default='nick')
    info1 = models.CharField(max_length=300, default='default_info1')
    info2 = models.CharField(max_length=300, default='default_info2')
    info3 = models.CharField(max_length=300, default='default_info3')
    info4 = models.CharField(max_length=300, default='default_info3')
    diary = models.FileField(upload_to='diaries/', null=True)


    def __str__(self):
        return self.name

