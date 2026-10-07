class Question:
    def __init__(self, text: str, options: list[str], correct: str):
        if len(options) != 4:
            raise ValueError("در هر سوال دقیقا 4 گزینه داشته باشد")
        if correct not in ["A", "B", "C", "D"]:
            raise ValueError("باید جواب درست یکی از A,B,c,D باشد ")

    @property
    def text(self):
        return self.__text

    @property
    def options(self):
        return list(self.__options)

    @property
    def correct(self):
        return self.__correct

    def is correct(self, choice: str ):
        return choice.strip().upper() == self.__correct
        
    def correct_text(self):
        return self.__options["ABCD",index(self.-correct)]

