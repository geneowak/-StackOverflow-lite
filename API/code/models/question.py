
class Question:

    questions = [
        {
            'id': 1,
            "title": "How do I become the best programmer in the universe?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "answers": [],
            "comments": []
        },
        {
            'id': 2,
            "title": "How do I join Andela?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "answers": [],
            "comments": []
        },
        {
            'id': 3,
            "title": "How can I hack into the C.I.A?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus quis sapien eu tempor.",
            "answers": [],
            "comments": []
        }
    ]

    def __init__(self, _id, title, body):
        self.id = _id
        self.title = title
        self.body = body
        self.answers = []

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "answers": self.answers
        }

    @classmethod
    def add_question(cls, data):
        question = {
            'id': data.id,  # using timestamps as ids
            "title": data.title,
            "body": data.body,
            "answers": []
        }
        print(question)
        cls.questions.append(question)
        return None

    ''' return True if answer is added, False otherwise '''
    @classmethod
    def add_answer (cls, questionId, answer):
        question = cls.get_question_by_id(questionId)

        if question:
            question['answers'].append(answer)
            return True
        return False

    @classmethod
    def get_question_by_id(cls, questionId):
        try:
            # check if question id is in required format
            questionId = float(questionId)
        except:
            return None
        for qn in cls.questions:
            if float(qn['id']) == questionId:
                return qn
        return None

    # get all the questions with their answers on loading the application
    @classmethod
    def load_all_qns(cls):
        from .answer import Answer
        for qn in cls.questions:
            qn['answers'].extend(Answer.get_answers_by_qn_id(qn['id']))


    @classmethod
    def get_questions(cls):
        return cls.questions
