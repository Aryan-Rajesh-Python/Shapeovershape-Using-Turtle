import turtle
import random
from turtle import Turtle,Screen
tortoise=Turtle()
screen=Screen()
colors=["red","green","blue","brown","pink","violet","yellow"]
def shapeovershape():
    def draw_shape(num_sides):
        a=(360/num_sides)
        for i in range(num_sides):
            tortoise.forward(100)
            tortoise.left(a)
    for i in range(3,15):
        tortoise.color(random.choice(colors))
        draw_shape(i)
    screen.exitonclick()
while(True):
    choice=input("Do you want to continue drawing shapeovershape: ")
    if(choice=="yes"):
        shapeovershape()
    else:
        print("Thank you for using our application!")
        break