from turtle import *
from random import randrange
from freegames import square, vector
#<<<<<<< HEAD

import random
#>>>>>>> RandomColors

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#<<<<<<< HEAD

color = random.choice(['black', 'yellow', 'magenta', 'blue', 'purple'])
colores = random.choice(['black', 'yellow', 'magenta', 'blue', 'purple'])
#>>>>>>> RandomColors


               
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."

    head = snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        #Aquí se define el movimiento aleatorio de la comida. Se utilizó un IF con diferentes condiciones para evitar que se salga de la caja.
        snake.pop(0)
        if food.x==190 and food.y==190:
            MC=vector(randrange(-1, 1),randrange(-1, 1))*10
            food.move(MC)
        elif food.x==-190 and food.y==-190:
            MC=vector(randrange(0, 2),randrange(0, 2))*10
            food.move(MC)
        elif food.x==190 and food.y==-190:
            MC=vector(randrange(-1, 1),randrange(0, 2))*10
            food.move(MC)
        elif food.x==-190 and food.y==190:
            MC=vector(randrange(0, 2),randrange(-1, 1))*10
            food.move(MC)
        elif food.x==190:
            MC=vector(randrange(-1, 1),randrange(-1, 2))*10
            food.move(MC)
        elif food.x==-190:
            MC=vector(randrange(0, 2),randrange(-1, 2))*10
            food.move(MC)
        elif food.y==190:
            MC=vector(randrange(-1, 2),randrange(-1, 1))*10
            food.move(MC)
        elif food.y==-190:
            MC=vector(randrange(-1, 2),randrange(0, 2))*10
            food.move(MC)
        else:
            MC=vector(randrange(-1, 2),randrange(-1, 2))*10
            food.move(MC)
    clear()

#<<<<<<< HEAD
    for body in snake:
        square(body.x, body.y, 9, 'black')

    for body in snake:#Aqui se dibuja toda la vibora
        square(body.x, body.y, 9, color) #falta ponerle color al body
#>>>>>>> RandomColors

    square(food.x, food.y, 9, colores)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
