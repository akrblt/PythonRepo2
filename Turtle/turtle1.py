import turtle

t=turtle.Turtle()

t.pencolor("red")
t.pensize(3)
t.write("Bonjour !", font=("Arial", 24, "bold"))
for i in range(100) :
    t.forward(200)
    t.right(90)
    if(i%2==0):
        t.pencolor("blue")
        t.forward(200)
        t.right(135)
    if(i%3==0):
        t.pencolor("orange")
        t.begin_fill()
    if(i%5==0):
        t.pencolor("yellow")



    else:

        t.pencolor("green")
        t.end_fill()


turtle.exitonclick()