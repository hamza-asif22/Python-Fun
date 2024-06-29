import turtle

def drawOlympicCircle(x, y, color, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)

def drawOlympicLogo(radius):
    positions = [
        (60, 0, 'blue'),
        (-60, 0, 'black'),
        (120, -60, 'red'),
        (0, -60, 'yellow'),
        (-120, -60, 'green')
    ]
    for position in positions:
        drawOlympicCircle(position[0], position[1], position[2], radius)

turtle.speed(6)
drawOlympicLogo(50)
turtle.done()
