import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently return false for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text='¿Cuál es la mejor compañia del mundo?', pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)