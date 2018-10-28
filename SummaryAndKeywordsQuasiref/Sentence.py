from stop_words import stop_words

class Sentence (object):

    def __init__(self, text, index):
        self.token=list()
        self.text=text
        self.index=index
        self.weight=0
        self.token_count=0
        self.dictionary = {}




