import turtle

a = []

def get_turtle_state(t):
    return t.heading(), t.position()

def restore(t, state):
    t.setheading(state[0])
    t.setposition(state[1][0], state[1][1])

def process(str, t):
    new = ""
    for c in str:
        if(c == 'X'):
            new += 'YF+XF+Y'
        elif c == 'Y':
            new += 'XF-YF-X'
        else:
            new += c
    return new

def createLSystem(Iters, axiom, t):
    create = axiom
    next = ""
    for i in range(Iters):
        next = process(create, t)
        create = next
        # print(i, create)
    
    return next

def drawLsystem(aTurtle, str, angle, dist):
    for c in str:
        if c == 'F':
            aTurtle.forward(dist)
        elif c == '+':
            aTurtle.right(angle)
        elif c == '-':
            aTurtle.left(angle)
        elif c == '[':
            a.append(get_turtle_state(aTurtle))
        elif c == ']':
            aTurtle.up()
            restore(aTurtle, a.pop())
            aTurtle.down()



def main():
    t = turtle.Turtle()
    inst = createLSystem(7, "YF", t)
    wn = turtle.Screen()

    t.up()
    t.forward(100)
    t.backward(0)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.right(90)
    t.down()
    t.speed(1000)
    drawLsystem(t, inst, 60, 2)

    wn.exitonclick()

main()
