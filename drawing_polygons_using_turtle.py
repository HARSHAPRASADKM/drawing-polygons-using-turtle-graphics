from turtle import Turtle , Screen

tim= Turtle()
tim.pencolor("red")
tim.forward(100)
def any_polygon(side):

    for _ in range(side):
        tim.right(360/side)
        tim.forward(100)
list_of_colors = ["red","orange","yellow","green","blue","violet","indigo","pink","purple","brown","black"]
for i in range(3,11):
    tim.pencolor(list_of_colors[i-3])
    any_polygon(i)


screen = Screen()
screen.exitonclick()