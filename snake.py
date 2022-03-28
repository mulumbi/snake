from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = 3
        self.body = []
        self.move = 20
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(self.segments):
            seg = Turtle(shape="square")
            seg.color("white")
            seg.penup()
            seg.setx(seg.xcor() - i * self.move)
            self.body.append(seg)

    def grow(self):
        # check which side the current last piece is heading and add accordingly

        last_seg = self.body[self.segments - 1]
        last_heading = last_seg.heading()
        if last_heading == UP:
            x = last_seg.xcor()
            y = last_seg.ycor() - self.move
        elif last_heading == DOWN:
            x = last_seg.xcor()
            y = last_seg.ycor() + self.move
        elif last_heading == LEFT:
            x = last_seg.xcor() + self.move
            y = last_seg.ycor()
        else:
            x = last_seg.xcor() - self.move
            y = last_seg.ycor()
        self.segments += 1
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(x, y)
        self.body.append(seg)

    def move_forward(self):
        for i in reversed(range(len(self.body))):
            # mainly control the head
            part = self.body[i]
            if i == 0:
                part.forward(self.move)
            else:
                prev = self.body[i - 1]
                prev_x = prev.xcor()
                prev_y = prev.ycor()
                part.setx(prev_x)
                part.sety(prev_y)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset_snake(self):
        for seg in self.body:
            seg.goto(4000, 4000)
        self.segments = 3
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
