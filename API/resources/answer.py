from flask import jsonify
from flask_restful import Resource, reqparse
from API.models.answer import Answer
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

        parser = reqparse.RequestParser()
        parser.add_argument(
            'body',
            type=str,
            required=True,
            help="The body field can't be empty"
        )

        data = parser.parse_args()
        # answer = {
        #     'id': time.time(),  # using timestamps as ids
        #     "qn_id": data['qn_id'],
        #     "body": data['body'],
        #     "comments": []
        # }
        timestamp = time.time()
        answer = Answer(timestamp,  data['body'], questionId)
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
