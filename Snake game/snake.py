from turtle import Turtle

STARTING_POSITIONS = [(i*-20, 0) for i in range(3)]
MOVES = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self, n: int):
        self.n = n
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        block = Turtle('square')
        block.penup()
        block.color('white')
        block.goto(position)
        self.segments.append(block)

    def extend(self):
        self.add_segment(self.segments[-1].position(    ))

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVES)


if __name__ == '__main__':
    pass
    # screen = Screen()
    # screen.setup(width=600, height=600)
    # screen.title("Snake game")
    # screen.bgcolor('black')
    # screen.tracer(0)
    # snake = Snake(3)
    # game_is_on = True
    # while game_is_on:
    #     screen.listen()
    #     screen.update()
    #     time.sleep(0.5)
    #     snake.move()
    #     snake.up()
    #     snake.move()
    # screen.exitonclick()
