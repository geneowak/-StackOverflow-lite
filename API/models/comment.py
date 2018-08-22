
class Comment:

    def __init__(self, _id, body, parent, parent_id):
        self.id = _id
        self.body = body
        self.parent = parent # NUM 'question', 'answer'
        self.parent_id = parent_id

    def json(self):
        return {
            "id": self.id,
            "body": self.body
        }
