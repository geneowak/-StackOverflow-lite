from .question import Question

class Answer:
    answers = [
        {
            'id': 1,
            "qn_id": 1,
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "comments": []
        },
        {
            'id': 2,
            "qn_id": 2,
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "comments": []
        },
        {
            'id': 3,
            "qn_id": 2,
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "comments": []
        }
    ]
    
    def __init__(self, _id, body, qn_id):
        self.id = _id
        self.body = body
        self.qn_id = qn_id
        self.comments = []

    def json(self):
        return {
            "id": self.id,
            "body": self.body,
            "comments": self.comments
        }

    @classmethod
    def add_answer(cls, answer):
        # first check if the question exists
        if Question.get_question_by_id(answer.qn_id):
            ans ={
                "id": answer.id,
                "body": answer.body,
                "qn_id": answer.qn_id,
                "comments": []
            }
            cls.answers.append(ans)
            try:
                Question.add_answer(answer.qn_id, ans)
            except:
                # return {'message': 'There was a problem adding an answer to the question'}, 500            
                return False
            return True
        return False

    @classmethod
    def get_answers(cls):
        return cls.answers

    @classmethod
    def get_answers_by_qn_id(cls, qn_id):
        return list(filter(lambda ans: ans['qn_id'] == qn_id, cls.answers))
        
