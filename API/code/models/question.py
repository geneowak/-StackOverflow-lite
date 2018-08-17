
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
        self.id = id
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
    def add_question(cls, question):
        cls.questions.append(question)
        return None

    @classmethod
    def get_question_by_id(cls, questionId):
        for qn in cls.questions:
            if str(qn['id']) == questionId:
                return {'question': qn}
        return None

    @classmethod
    def get_questions(cls):
        return cls.questions
