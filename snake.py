from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for m in START_POSITION:
            self.add_segment(m)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def move(self):
        # ''' Move snake forward one step '''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        # Extend snake by one segment on tail
        self.add_segment(self.segments[-1].position())

    def up(self):
        # ''' Move snake head pointing up '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        # ''' Move snake head pointing left '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        # ''' Move snake head pointing down '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # ''' Move snake head pointing right '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
