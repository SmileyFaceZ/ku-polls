import datetime

from django.test import TestCase
from django.utils import timezone
from polls.models import Question


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


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self) -> None:
        """
        was_published_recently() returns False for questions whose pub_date is
        in the future.
        """
        future_question = create_question(days=30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self) -> None:
        """
        was_published_recently() returns False for questions whose pub_date is
        older than 1 day.
        """
        old_question = create_question(days=1, seconds=1)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self) -> None:
        """
        was_published_recently() returns True for questions whose pub_date is
        within the last day.
        """
        recent_question = create_question(hours=-23, minutes=-59, seconds=-59)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_is_published_question_with_future(self) -> None:
        """
        is_published() returns False for questions with a publication
        date in the future.
        """
        future_question = create_question(seconds=1)
        self.assertEqual(future_question.is_published(), False)

    def test_is_published_question_with_now(self) -> None:
        """
        is_published() returns True for questions with a publication
        date set to now.
        """
        current_question = create_question()
        self.assertEqual(current_question.is_published(), True)

    def test_is_published_question_with_past(self) -> None:
        """
        is_published() returns True for questions with a publication
        date in yesterday.
        """
        past_question = create_question(days=-1)
        self.assertEqual(past_question.is_published(), True)

    def test_cannot_vote_after_end_date(self) -> None:
        """
        can_vote() returns False for questions with an
        end date that has already passed.
        """
        future_question = create_question(end_time=-7)
        self.assertEqual(future_question.can_vote(), False)

    def test_can_vote_in_time(self) -> None:
        """
        can_vote() returns True for questions within the voting period.
        """
        in_time_question = create_question(end_time=1)
        self.assertEqual(in_time_question.can_vote(), True)

    def test_cannot_vote_before_pub_date(self) -> None:
        """
        can_vote() returns False for questions that have not yet
        reached their publication date.
        """
        before_vote_question = create_question(
            days=30,
            hours=23,
            minutes=59,
            seconds=59
        )
        self.assertEqual(before_vote_question.can_vote(), False)
