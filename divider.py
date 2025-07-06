from turtle import Turtle

class Divider(Turtle):
     def __init__(self):
         super().__init__()
         self.color("white")
         self.ht()
         self.penup()
         self.goto(0,300)
         self.setheading(270)
         self.dash_line()


     def dash_line(self):
         for _ in range(30):
             self.pendown()
             self.forward(10)
             self.penup()
             self.forward(10)
