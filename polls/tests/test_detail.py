import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from polls.models import Question
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
            pub_date=time
        )

    time_end = timezone.now() + datetime.timedelta(days=end_time)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time,
        end_date=time_end
    )


class QuestionDetailViewTests(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.client = Client()
        cls.user = User.objects.create_user(username='test', password='test')

    def test_future_question(self) -> None:
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        self.client.login(username='test', password='test')
        future_question = create_question(
            question_text='Future question.',
            days=5
        )
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self) -> None:
        """
        The detail view of a question with a pub_date in
        the past displays the question's text.
        """
        self.client.login(username='test', password='test')
        past_question = create_question(
            question_text='Past Question.',
            days=-5
        )
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
