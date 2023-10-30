import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """  Represents a poll question and contains the question text,
    publish date, and end date for voting.
    """
    objects = None
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    end_date = models.DateTimeField("end date", null=True, blank=True)

    def was_published_recently(self) -> bool:
        """
        Returns True if the question was published within the last day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self) -> str:
        return self.question_text

    def is_published(self) -> bool:
        """
        Returns True if the question is published.
        """
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self) -> bool:
        """
        Returns True if the question is published and the current time is
        between the publication date and end date.
        """
        if self.end_date is None:
            return self.is_published()

        now = timezone.now()
        return self.pub_date <= now <= self.end_date

