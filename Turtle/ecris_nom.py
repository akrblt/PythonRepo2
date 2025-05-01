import turtle

t = turtle.Turtle()
t.color("blue")
t.pensize(3)

# Écrire un nom
t.penup()
t.goto(-50, 100)
t.pendown()
t.write("Bonjour !", font=("Arial", 24, "bold"))

# Dessiner une étoile
for i in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
