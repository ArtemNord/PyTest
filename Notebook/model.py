from datetime import datetime


class Note:

    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M")

    def __str__(self):
        return f'{self.date}\n{self.title}\n{self.text}'