class Post:

    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text

    def some_function(self):
        print(self.title)

    def new_function(self):
        print('Version 3')
