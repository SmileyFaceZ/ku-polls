import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from polls.models import Question, Choice
from django.contrib.auth.models import User


def create_question(question_text="",
                    days=0, hours=0, minutes=0, seconds=0,
                    end_time=None) -> Question:
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    if end_time is None:
        return Question.objects.create(
            question_text=question_text,
            pub_date=time)

    time_end = timezone.now() + datetime.timedelta(days=end_time)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time,
        end_date=time_end
    )


class QuestionVotingTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'test'
        self.password = 'test'
        self.question = create_question(question_text='Question')
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text='Choice1'
        )

    def test_vote_with_login(self) -> None:

        User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.client.login(username=self.username, password=self.password)

        url = reverse('polls:vote', args=(self.question.id,))
        response = self.client.post(url, {'choice': self.choice.id})

        self.assertEqual(response.status_code, 302)

        choice_vote = Choice.objects.get(id=self.choice.id)
        self.assertEqual(choice_vote.votes, 1)

    def test_vote_with_no_login(self) -> None:

        url = reverse('polls:vote', args=(self.question.id,))
        response = self.client.post(url, {'choice': self.choice.id})

        self.assertEqual(response.status_code, 302)

        choice_vote = Choice.objects.get(id=self.choice.id)
        self.assertEqual(choice_vote.votes, 0)
