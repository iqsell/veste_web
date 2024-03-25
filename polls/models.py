from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Product(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.JSONField()
    sizes = models.JSONField()
    photo = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)
