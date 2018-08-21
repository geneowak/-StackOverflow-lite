from flask import jsonify
from flask_restful import Resource, reqparse
from API.models.answer import Answer
from API.models.question import Question
from .utilities import clean_input
import time

# load the answers from Model....
answers = Answer.get_answers()


class Answers(Resource):
    # add a answer given its ID
    def get(self):
        pass

    def post(self, questionId):
        # check if the submitted questionId is in the expected format
        try:
            questionId = float(questionId)
        except:
            return { "message": "The question id should be a float"}, 400
        
        # check if the question exists
        if not Question.get_question_by_id(questionId):
            return {"message": "Sorry, that question doesn't exist"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument(
            'body',
            type=str,
            required=True,
            help="The body field can't be empty"
        )

        data = parser.parse_args()
        ''' validate data sent '''
        if not clean_input(data['body']):
            return {'message': 'The body should be a string'}, 400
        
        ''' validate that the question hasn't been asked before '''
        if Answer.check_ans_body(data['body'], questionId):
            return {'message': 'Sorry, that answer has already been given'}, 400
        # setting ids
        ans_id = Answer.get_no_of_ans() + 1
        answer = Answer(ans_id,  data['body'], questionId)
        try:
            if Answer.add_answer(answer) == True:
                return {'message': 'Your answer was successfully added'}, 201
        except:
            return {'message': 'There was a problem adding the answer'}, 500

        return {'message': 'There was a problem adding the answer'}, 500

    def put(self):
        pass

    def delete(self):
        pass


class AnswerList(Resource):
    # get all the available answers
    def get(self):
        return {'answers': Answer.get_answers()}
    # add a answer

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
