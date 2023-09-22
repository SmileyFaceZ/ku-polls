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
            pub_date=time
        )

    time_end = timezone.now() + datetime.timedelta(days=end_time)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time,
        end_date=time_end
    )


class UserAuthTest(TestCase):

    def setUp(self):
        super().setUp()
        self.username = "testuser"
        self.password = "FatChance!"
        self.user1 = User.objects.create_user(
            username=self.username,
            password=self.password,
            email="testuser@nowhere.com"
        )
        self.user1.first_name = "Tester"
        self.user1.save()
        self.question = create_question(question_text="First Poll Question")
        for n in range(1, 4):
            choice = Choice(choice_text=f"Choice {n}", question=self.question)
            choice.save()

    def test_logout(self):
        """A user can logout using the logout url.

        As an authenticated user,
        when I visit /accounts/logout/
        then I am logged out
        and then redirected to the login page.
        """
        logout_url = reverse("logout")

        self.assertTrue(
            Client().login(username=self.username, password=self.password)
        )
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('login'))

    def test_login_view(self):
        """A user can login using the login view."""
        login_url = reverse("login")
        response = self.client.get(login_url)
        self.assertEqual(200, response.status_code)
        form_data = {"username": "testuser",
                     "password": "FatChance!"
                     }
        response = self.client.post(login_url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('polls:index'))

    def test_auth_required_to_vote(self):
        """Authentication is required to submit a vote.

        As an unauthenticated user,
        when I submit a vote for a question,
        then I am redirected to the login page
          or I receive a 403 response (FORBIDDEN)
        """
        vote_url = reverse('polls:vote', args=[self.question.id])

        choice = self.question.choice_set.first()

        form_data = {"choice": choice.id}
        response = self.client.post(vote_url, form_data)

        self.assertEqual(response.status_code, 302)

        url_login = reverse('login')
        login_with_next = f"{url_login}?next={vote_url}"
        self.assertRedirects(response, login_with_next)
