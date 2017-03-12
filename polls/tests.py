import datetime
from django.test import TestCase
from .models import Question
from django.utils import timezone


class QuestionMethodsTest(TestCase):
	def test_wasPublished_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(publish_date=time)
		self.assertIs(future_question.wasPublished_recently(), False)


	def test_wasPublished_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(publish_date=time)
		self.assertIs(old_question.wasPublished_recently(), False)


	def test_wasPublished_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(publish_date=time)
		self.assertIs(recent_question.wasPublished_recently(), True)
