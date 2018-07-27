def hey(phrase):
    sentence = SentenceThinker(phrase.strip())

    if sentence.is_silence():
        return "Fine. Be that way!"
    elif sentence.is_yelling() and sentence.is_question():
        return "Calm down, I know what I'm doing!"
    elif sentence.is_question():
        return "Sure."
    elif sentence.is_yelling():
        return "Whoa, chill out!"
    else:
        return "Whatever."

class SentenceThinker(object):

    def __init__(self, sentence):
        self.sentence = sentence

    def is_yelling(self):
        return self.sentence.isupper()

    def is_question(self):
        return self.sentence.endswith("?")

    def is_silence(self):
        return not self.sentence
