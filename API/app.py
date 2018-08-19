from flask import Flask
from flask_restful import Api

from resources.question import Questions, QuestionList
from resources.answer import Answers, AnswerList
from models.question import Question

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
@app.before_first_request
def load_data():
    #  first load all the questions with their repective answers
    Question.load_all_qns()

api.add_resource(Questions, '/api/v1/questions/<string:questionId>')
api.add_resource(QuestionList, '/api/v1/questions')
api.add_resource(AnswerList, '/api/v1/answers')
api.add_resource(Answers, '/api/v1/questions/<string:questionId>/answers')


''' start the app '''
if __name__ == "__main__":
    app.run(debug=True)
