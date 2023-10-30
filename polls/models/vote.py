from django.db import models
from .choice import Choice


class Vote(models.Model):
    """ Records a vote of a Choice ny a User. """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} voted for {self.choice.choice_text}"
