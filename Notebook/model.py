from datetime import datetime

class Note:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text
        self.data = datetime.now().strftime("%d.%m.%Y %H:%M")

    def __str__(self):
        return f'{self.data}\n{self.title}\n{self.text}'
