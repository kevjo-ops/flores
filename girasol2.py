import math
import turtle

# Configuración inicial de Turtle
turtle.bgcolor("#0B3D91")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(0)
turtle.fillcolor("orangered")

# Escribir el mensaje en la parte superior central
turtle.penup()
turtle.goto(0, 250)  # Posicionar el texto en la parte superior
turtle.pencolor("black")
turtle.write("Muchas gracias x todo Rosa", align="center", font=("Arial", 24, "bold"))
turtle.pendown()

# Parámetro phi para el ángulo dorado
phi = 137.508 * (math.pi / 180.0)

# Bucle para generar el patrón espiral
for i in range(180 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.left(-5)
        turtle.circle(500, 25)
        turtle.right(-155)
        turtle.circle(500, 25)
        turtle.end_fill()

turtle.hideturtle()
turtle.done()
