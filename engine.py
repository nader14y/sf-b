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
    
ROUND=5
TIMELIMIT = 30
POINTS = 10
SPEED_BONUS = 3
class Match:
    def __init__(self, player1, player2, questions):
        self.__players: list[str] = [player1, player2]
        self.__questions: list[Question] = list(questions)
        self.__scores: dict[str, int] = {player1: 0, player2: 0}
        self.__round: int = 0
        self.__answers: dick[str, tuple[str, float]] = {}

    @property
    def players(self):
        return list(self.__players)

    @property
    def round(self):
        return self.__round


    def score_of(self, player: str):
        """برای امتیاز"""
        return self.__scores[player]

    def answer_of(self, player: str):
        """جواب یک سوال"""
        return self.__answers[player]   

    def start_raund(self):
        self.__round += 1
        self.__answers ={}
    return self.__questions[self.__round -1]

    def submit(self, player: str, choice: str, elapsed: float ):
        """ چند ثانیه طول کشید وجواب یک بازیکن را ثبت کن"""
        self.__answers[player] = (choice, elapsed)

    def is_over(self):
        """برسی اتمام بازی """
        return self.__round >= ROUND

    def winner(self):
        """نمایش برنده در صورت مساوی هیج کدام"""
        player1, player2 = self.__players
        if self.__scores[player1] == self.__[player2]:
            return Nome 
        if self.__scores[player1] > self.__scores[player2]:
            return player1
        return player2

    def resolve_round(self):
        """برای ثبت نتیجه کل بازی"""
        question: Question = self.__questions[self.__round -1]
        results: dict[str, RoundResult] = {}
        correct_players: list[str]= []
        for player in self.__players:
            choice, elapsed = self.__answers[player]

            if elapsed > TIMELIMIT:
                results[player] = RoundResult("too_late", 0)
            elif Question.is_correct(choice):
                results[player] = RoundResult("correct, POINTS")
                correct_players.append(player)
            else:
                results[player] = RoundResult("wrong", 0)

class RoundResult:
    """ نتبجه یک بازیکن در راند"""
    def __init__(self, status: str, points: int):
        self.__status=status
        self.__points=points
    @property
    def status(self):
        return self.__status
        
    @property
    def points(self):
        return self.__points

    def add_bonus(self, amount: int):

        self.__points += amount
