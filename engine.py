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
    
ROUNDS = 5
class Match:
    def __init__(self,player1,player2,questions):
        if player1 == player2:
            raise ValueError("نام دو بازیکن نمی تواند یکی باشد")
        if len(questions) < ROUNDS:
            raise ValueError(f"tedad soal baiad kam tar az tedad soal bashad")

        self.__players: list[str] = [player1, player2]
        self.__questions: list[Question] = list(questions)
        self.__scores: dict[str, int] = {player1: 0, player2: 0}
        self.__round: int = 0
        self.__answers: dict[str, tuple[str, float]] = {}

    @property
    def players(self):
        return list(self.__players)

    @property
    def round(self):
        return self.__round 