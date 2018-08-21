import os
import unittest
from API.app import app
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
import json

class BaseCase(unittest.TestCase):
    # setup method
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.test_question = {
            "title": "How do I become the best programmer in the universe?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        self.test_answer = {
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }

    def test_get_questions(self):
        """ test that api can get questions """
        with self.client as client:
            # add a questions
            request = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(request.status_code, 201)
            request = client.post('/api/v1/questions', data={ "title": "some title", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = client.get('/api/v1/questions')
            self.assertEqual(request.status_code, 200)
            response = json.loads(request.data.decode())
            self.assertEqual(2, len(response['questions']))

    def test_add_question(self):
        """ test that api can add a question """
        with self.client as client:
            # add a questions
            request = client.post('/api/v1/questions', data=self.test_question)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            self.assertEqual(request.status_code, 201)

    def test_add_answer(self):
        " test that an answer can be added to a question "
        with self.client as client:
            # add a question
            request = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            request = client.post('/api/v1/questions/1/answers', data=self.test_answer)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Your answer was successfully added", response['message'])

    def test_get_question(self):
        """ test that api can get questions """
        with self.client as client:
            # add a questions
            request = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = client.get('/api/v1/questions/1')
            self.assertEqual(request.status_code, 200)
            self.assertIn("How do I become the best programmer in the universe?", str(request.data))

    def test_for_correct_qn_title(self):
        ''' test to ensure that the title of the question is a string '''
        with self.client as client:
            # check with empty title
            request = client.post('/api/v1/questions', data={ "title": " ", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])
            # check with numerical title
            request = client.post('/api/v1/questions', data={ "title": "21948", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])

    def test_for_repeated_qn(self):
        ''' test to ensure that a question isn't repeated '''
        with self.client as client:
            # post a question
            request = client.post('/api/v1/questions', data={'title':'title1', 'body':'body1'})
            self.assertEqual(request.status_code, 201)
            # check with repeated question title
            request = client.post('/api/v1/questions', data={'title':'title1', 'body':'body2'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that title has already been asked", response['message'])
            # check with repeated question body
            request = client.post('/api/v1/questions', data={'title':'title2', 'body':'body1'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that body has already been asked", response['message'])

    def test_for_correct_qn_body(self):
        ''' test if for if app rejects blank or numeric bodies for the question '''
        with self.client as client:
            # check with empty title
            request = client.post('/api/v1/questions', data={ "title": "tiltle", "body": " "})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            # check with numerical title
            request = client.post('/api/v1/questions', data={ "title": "tiltle", "body": "2356"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_blank_ans_body(self):
        with self.client as client:
            # add a questions
            request = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            # check with numerical body
            request = client.post('/api/v1/questions/1/answers', data={"body": "2356"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            # check with blank body
            request = client.post('/api/v1/questions/1/answers', data={"body": " "})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_repeated_answer(self):
        # add a question
        with self.client as client:
            request = client.post('/api/v1/questions', data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            request = client.post('/api/v1/questions/1/answers', data=self.test_answer)
            self.assertEqual(request.status_code, 201)
            request = client.post('/api/v1/questions/1/answers', data=self.test_answer)
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, that answer has already been given", response['message'])

    def test_qn_for_answer_exists(self):
        " test that an answer can be added to a question "
        with self.client as client:
            # add an answer before adding question
            request = client.post('/api/v1/questions/1/answers', data=self.test_answer)
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, that question doesn't exist", response['message'])

    def tearDown(self):
        Question.questions.clear()
        Answer.answers.clear()

