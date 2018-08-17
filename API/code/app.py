from flask import Flask
from flask_restful import Api

from resources.question import Questions, QuestionList

app = Flask(__name__)
app.secret_key = "AndelA11"
api = Api(app)

''' 
# end points to develop

GET /questions Fetch all questions
GET /questions/<questionId> Fetch a specific question
POST /questions Add a question
POST /questions/<questionId>/answers Add an answer

 '''

api.add_resource(Questions, '/api/v1/questions/<string:questionId>')
api.add_resource(QuestionList, '/api/v1/questions')


''' start the app '''
if __name__ == "__main__":
    app.run(debug=True)
