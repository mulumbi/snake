from turtle import Turtle

FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.game_state = True
        self.penup()
        self.hideturtle()
        self.color("White")
        self.draw_border()
        self.goto(0, 320)
        self.write(f"Score: {self.score} , High Score: {self.high_score}", align="center", font=FONT)

    def draw_border(self):
        self.setheading(0)
        self.goto(-310, -310)
        self.pendown()
        for i in range(4):
            self.forward(620)
            self.left(90)
        self.penup()

    def update_score(self):
        self.score += 1
        self.clear()
        self.draw_border()
        self.goto(0, 320)
        self.write(f"Score: {self.score} , High Score: {self.high_score}", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 10, "bold"))
        self.game_state = False
