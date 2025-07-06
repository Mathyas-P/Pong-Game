from turtle import Turtle
WINNING_POINT=10
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.left_score=0
        self.right_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 50, "normal"))

    def add_left_point(self):
        self.left_score+=1
        self.update()

    def add_right_point(self):
        self.right_score+=1
        self.update()

    def winner(self):
        if self.left_score==WINNING_POINT:
            winner="Left Player"
        else:
            winner="Right Player"
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0,0)
        self.write(f"{winner} Wins!", align="center", font=("Courier", 32, "bold"))
