from flask import jsonify
from flask_restful import Resource, reqparse
from models.answer import Answer
import time

# load the answers from Model....
answers = Answer.get_answers()


class Answers(Resource):
    # add a answer given its ID
    def get(self, answerId):
        for qn in answers:
            if str(qn['id']) == answerId:
                return {'answer': qn}
        return {'message': 'Question not found'}, 404

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class AnswerList(Resource):
    # get all the available answers
    def get(self):
        return {'answers': answers}
    # add a answer

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'qn_id',
            type=float,
            required=True,
            help="The qn_id field can't be empty"
        )
        parser.add_argument(
            'body',
            type=str,
            required=True,
            help="The body field can't be empty"
        )

        data = parser.parse_args()
        answer = {
            'id': time.time(),  # using timestamps as ids
            "qn_id": data['qn_id'],
            "body": data['body'],
            "comments": []
        }
        answers.append(answer)

        return {'message': 'Question was successfully created'}, 201

    def put(self):
        pass

    def delete(self):
        pass
