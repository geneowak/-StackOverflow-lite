from flask import jsonify
from flask_restful import Resource, reqparse
from API.models.question import Question
import time

class Questions(Resource):
    # add a question given its ID
    def get(self, questionId):
        qn = Question.get_question_by_id(questionId)
        if qn:
            return { 'question': qn }
        return { 'message': 'Question not found' }, 404

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class QuestionList(Resource):
    # get all the available questions
    def get(self):
        return {'questions': Question.get_questions()}, 200
        
    # add a question
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title', 
            type=str, 
            required=True,
            help="The title field can't be empty"
        )
        parser.add_argument(
            'body',
            type=str, 
            required=True,
            help="The body field can't be empty"
        )

        data = parser.parse_args()
        # using timestamps as ids
        timestamp = time.time()
        question = Question(timestamp, data['title'], data['body'])

        try:
            Question.add_question(question)
        except:
            return {'message': 'There was a problem adding the question'}, 500

        return {'message': 'Question was successfully created'}, 201

    def put(self):
        pass

    def delete(self):
        pass
