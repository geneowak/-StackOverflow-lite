
class Question:

    def __init__(self, _id, title, body, qn_id):
        self.id = id
        self.title = title
        self.body = body

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
