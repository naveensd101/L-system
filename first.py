import turtle

def process(str):
    new = ""
    for c in str:
        if(c == 'F'):
            new += 'F-F++F-F'
        else:
            new += c
    return new

def createLSystem(Iters, axiom):
    create = axiom
    next = ""
    for i in range(Iters):
        next = process(create)
        create = next
        # print(i, create)
    
    return next

def drawLsystem(aTurtle, str, angle, dist):
    for c in str:
        if c == 'F':
            aTurtle.forward(dist)
        elif c == 'B':
            aTurtle.backward(dist)
        elif c == '+':
            aTurtle.right(angle)
        elif c == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.backward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.right(90)
    t.right(90)
    t.down()
    t.speed(200)
    drawLsystem(t, inst, 60, 5)

    wn.exitonclick()

main()