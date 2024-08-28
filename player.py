from turtle import Turtle, Screen

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 230





#Asking user for the input


class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.setup(500, 400)
        user_color = screen.textinput("Turtle Color",
                                    "Choose your turtle's colour. 'Red', 'Yellow' or 'Green'")
        self.shape("turtle")
        self.color(user_color)
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


