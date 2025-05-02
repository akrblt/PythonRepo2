import turtle

t = turtle.Turtle()
t.color("red")
t.pensize(3)

# Écrire un nom
t.penup()
t.goto(-50, 200)
t.pendown()
t.write("salut ANTHO ! Merci ", font=("Arial", 24, "bold"))
t.penup()
t.goto(-10,150)
t.pendown()
# Dessiner une étoile
for i in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
