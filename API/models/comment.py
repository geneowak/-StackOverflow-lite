
class Comment:

    def __init__(self, _id, body, parent, parent_id):
        self.id = _id
        self.body = body
        self.parent = parent # this identifies whether the comment belongs to a question or an answer
        self.parent_id = parent_id

    def json(self):
        return {
            "id": self.id,
            "body": self.body
        }
