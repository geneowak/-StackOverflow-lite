import unittest
from API.app import app
from API.resources.question import QuestionList
from API.models.question import Question
import json

class BaseCase(unittest.TestCase):
    # setup method
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.test_question = {
            'id': 1,
            "title": "How do I become the best programmer in the universe?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "answers": [],
            "comments": []
        }
        self.test_answer = {
            'id': 2,
            "qn_id": 2,
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "comments": []
        }

    def test_get_questions(self):
        """ test that api can get questions """
        with self.client as client:
            # first post some data
            req = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(req.status_code, 201)
            # try getting the data submitted
            req = client.get('/api/v1/questions')
            self.assertEqual(req.status_code, 200)
            self.assertIn(
                "How do I become the best programmer in the universe?", str(req.data))

    def test_add_question(self):
        """ test that api can add a question """
        with self.client as client:
            # post some data
            req = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(req.status_code, 201)
            response_json = json.loads(req.data.decode())
            self.assertIn("Question was successfully created", response_json['message'])
