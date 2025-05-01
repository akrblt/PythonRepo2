import turtle
import time
import random

# Ekranı ayarla
ekran = turtle.Screen()
ekran.title("Basit Snake Oyunu")
ekran.bgcolor("black")
ekran.setup(width=600, height=600)
ekran.tracer(0)

# Yılan kafası
kafa = turtle.Turtle()
kafa.shape("square")
kafa.color("green")
kafa.penup()
kafa.goto(0, 0)
kafa.direction = "stop"

# Yem (yemek)
yem = turtle.Turtle()
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(100, 0)

# Hareket fonksiyonu
def hareket():
    if kafa.direction == "up":
        kafa.sety(kafa.ycor() + 20)
    if kafa.direction == "down":
        kafa.sety(kafa.ycor() - 20)
    if kafa.direction == "left":
        kafa.setx(kafa.xcor() - 20)
    if kafa.direction == "right":
        kafa.setx(kafa.xcor() + 20)

# Yön kontrolü
def yukari(): kafa.direction = "up"
def asagi(): kafa.direction = "down"
def sola(): kafa.direction = "left"
def saga(): kafa.direction = "right"

ekran.listen()
ekran.onkeypress(yukari, "Up")
ekran.onkeypress(asagi, "Down")
ekran.onkeypress(sola, "Left")
ekran.onkeypress(saga, "Right")

# Oyun döngüsü
while True:
    ekran.update()
    hareket()

    # Yılan yemi yerse
    if kafa.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

    # Duvara çarparsa
    if abs(kafa.xcor()) > 290 or abs(kafa.ycor()) > 290:
        kafa.goto(0, 0)
        kafa.direction = "stop"

    time.sleep(0.1)
