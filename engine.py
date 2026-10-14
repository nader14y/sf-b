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
ROUNDS=5
class Match:
    def __init__(self,player1:str,player2:str, questions: list[Question])
        if player1 == player2:
            raise ValueError(" نام دو بازیکن نمی تواند یکی باشد")
        if len(question) < ROUNDS:
            raise ValueError(f"for {ROUNDS} at least , round {ROUNDS} question is needed")
        self._players: list[str] = [player1,player2]
        self._questions:list[Question] = list(questions)
        self._scores:dict [str,int] = {player1: 0,player2:0}
        self._round: int=0
        self._answers:dict [str,tuple[str,float]] = {}
    @property
    def players(self):
        return list(self._players)
    @property
    def round(self):
        return self._round
    def score_of(self,player:str):
        return self._scores[player]
    def answer_of(self,players:str):
        return self._answers[players]
