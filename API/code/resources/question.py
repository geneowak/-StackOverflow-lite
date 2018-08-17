from flask import jsonify
from flask_restful import Resource, reqparse

questions = [
    {
        'id':1,
        "title": "How do I become the best programmer in the universe?",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor. Suspendisse vestibulum felis vel ornare porttitor. Duis at tellus facilisis, mollis mi sit amet, porta quam. Integer sit amet pellentesque quam, non volutpat lectus. Vivamus hendrerit justo sed augue viverra, elementum maximus tortor vehicula. Donec vitae sem odio. Donec sed eros eu ipsum pulvinar congue. Sed arcu sapien, mollis quis sodales et, pharetra at est."
    },
    {
        'id':2,
        "title": "How do I join Andela?",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor. Suspendisse vestibulum felis vel ornare porttitor. Duis at tellus facilisis, mollis mi sit amet, porta quam. Integer sit amet pellentesque quam, non volutpat lectus. Vivamus hendrerit justo sed augue viverra, elementum maximus tortor vehicula. Donec vitae sem odio. Donec sed eros eu ipsum pulvinar congue. Sed arcu sapien, mollis quis sodales et, pharetra at est."
    },
    {
        'id':3,
        "title": "How can I hack into the C.I.A?",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor. Suspendisse vestibulum felis vel ornare porttitor. Duis at tellus facilisis, mollis mi sit amet, porta quam. Integer sit amet pellentesque quam, non volutpat lectus. Vivamus hendrerit justo sed augue viverra, elementum maximus tortor vehicula. Donec vitae sem odio. Donec sed eros eu ipsum pulvinar congue. Sed arcu sapien, mollis quis sodales et, pharetra at est."
    }
]

class Question(Resource):
    # parser = reqparse.RequestParser()
    
    def get(self, questionId):
        for qn in questions:
            if str(qn['id']) == questionId:
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
        return {'questions': questions}
