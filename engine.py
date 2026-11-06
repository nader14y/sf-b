class Question:
    def __init__(self,text,options,correct):

        self._text=text
        self._options=list(options)
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
        return choice.strip().upper() == self._correct
    def correct_text(self):
        return self._options["ABCD".index(self._correct)]


class RoundResult:

    def __init__(self, status: str, points: int) -> None:
        self._status: str = status                 # "correct" یا "wrong" یا "too_late"
        self._points: int = points
    @property
    def status(self) -> str:
        return self._status
    @property
    def points(self) -> int:
        return self._points
    def add_bonus(self, amount: int) -> None:
        """امتیاز اضافه — تنها راهِ مجاز برای عوض‌کردن points."""
        self._points += amount

ROUNDS = 5
TIME_LIMIT = 30
POINTS = 10
SPEED_BONUS = 3

class Match:
    """یک مسابقه‌ی دونفره‌ی ۵ راندی."""
    
    def __init__(self, player1: str, player2: str, questions: list[Question]) -> None:
        if player1 == player2:
            raise ValueError("نام دو بازیکن نمی‌تواند یکی باشد")
        if len(questions) < ROUNDS:
            raise ValueError(f"برای {ROUNDS} راند، حداقل {ROUNDS} سؤال لازم است")

        self._players: list[str] = [player1, player2]
        self._questions: list[Question] = list(questions)
        self._scores: dict[str, int] = {player1: 0, player2: 0}
        self._round: int = 0                                   # ۰ یعنی هنوز شروع نشده
        self._answers: dict[str, tuple[str, float]] = {}       # نام → (گزینه، ثانیه)

    @property
    def players(self) -> list[str]:
        return list(self._players)

    @property
    def round(self) -> int:
        return self._round

    def score_of(self, player: str) -> int:
        return self._scores[player]

    def answer_of(self, player: str) -> tuple[str, float]:
        """(گزینه‌ای که زد، چند ثانیه طول کشید)"""
        return self._answers[player]
    
    def start_round(self) -> Question:
        """شروع راند بعدی و برگرداندن سؤال آن."""
        self._round += 1
        self._answers = {}
        return self._questions[self._round - 1]

    def submit(self, player: str, choice: str, elapsed: float) -> None:
        """جواب یک بازیکن را ثبت می‌کند. elapsed = چند ثانیه طول کشید."""
        self._answers[player] = (choice, elapsed)

    def is_over(self) -> bool:
        """بررسی اتمام بازی"""
        return self._round >= ROUNDS

    def winner(self) -> str | None:
        """نمایش برنده. در صورت مساوی هیچکدام را برمیگرداند"""
        player1, player2 = self._players
        if self._scores[player1] == self._scores[player2]:
            return None
        if self._scores[player1] > self._scores[player2]:
            return player1
        return player2

    def resolve_round(self) -> dict[str, RoundResult]:
        """برای ثبت نتیجه بازی"""
        question = self._questions[self._round - 1]
        results: dict[str, RoundResult] = {}
        correct_players: list[str] = []

        # ۱) درست بود، غلط بود، یا دیر؟
        for player in self._players:
            choice, elapsed = self._answers[player]

            if elapsed > TIME_LIMIT:
                results[player] = RoundResult("too_late", 0)
            elif question.is_correct(choice):
                results[player] = RoundResult("correct", POINTS)
                correct_players.append(player)
            else:
                results[player] = RoundResult("wrong", 0)

        # ۲) بونوس سرعت: بین درست‌جواب‌ها، سریع‌ترین
        if correct_players:
            fastest = correct_players[0]
            for player in correct_players:
                if self._answers[player][1] < self._answers[fastest][1]:
                    fastest = player
            results[fastest].add_bonus(SPEED_BONUS)

        # ۳) امتیازها را جمع کن  ← اینجا، *داخل* موتور، مجاز است
        for player in self._players:
            self._scores[player] += results[player].points

        return results
        
