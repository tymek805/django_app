from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    published_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    num_of_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
