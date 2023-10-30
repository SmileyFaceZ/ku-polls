from django.db import models
from .question import Question


class Choice(models.Model):
    """ Represents a choice for a poll question. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self) -> int:
        return self.vote_set.count()

    def __str__(self) -> str:
        return self.choice_text
