class Question:
    def __init__(self,text,options,correct):

        self._text=text
        self._option=list(options)
        self._correct=correct

    @property
    def text(self):
        return self._text
    @property
    def options(self):
        return list(self._options)
    @property
    def correct(self):
        return self._correct
    def is_correct(self,choice):
        return choice.strip().upper == self._correct
    def correct_text(self):
        return self._option["ABCD".index(self._correct)]
    

        
