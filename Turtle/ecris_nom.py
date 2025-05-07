import turtle

t = turtle.Turtle()
t.color("red")
t.pensize(3)

# Écrire un nom
t.penup()
t.goto(-150, 300)
t.pendown()
t.write("SALUT TOUTE LE MONDE ", font=("Arial", 24, "bold"))
t.penup()
t.goto(-50,-50)
t.pendown()
# Dessiner une étoile
for i in range(100) :
    t.forward(200)
    t.right(90)
    if(i%2==0):
        t.pencolor("blue")
        t.forward(200)
        t.right(135)
    if(i%3==0):
        t.pencolor("orange")
       # t.begin_fill()
    if(i%5==0):
        t.pencolor("yellow")



    else:

        t.pencolor("green")
        t.end_fill()

turtle.done()
