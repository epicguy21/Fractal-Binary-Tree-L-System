import turtle

stackX = []
stackY = []
stackA = []

def genTree(tree, recursions, i):
    if (i >= recursions):
        return tree
    else:
        newTree = "";
        for char in tree:
            if (char == "1"):
                newTree += "11"
            else: 
                if (char == "0"):
                    newTree += "1[0]0"
                else:
                    newTree += char;
                
        return genTree(newTree, recursions, i+1)
        
def drawTree(tree):
    t.width(width)
    t.pendown()
    t.left(90)
    for char in tree:
        if (char == "0"):
            t.pencolor("green")
            t.forward(length)
        else:
            if (char == "1"):
                t.pencolor("black")
                t.forward(length)
            else:
                if (char == "]"):
                    lastIndex = len(stackX) - 1
                    t.penup()
                    t.goto(stackX[lastIndex], stackY[lastIndex])
                    t.setheading(stackA[lastIndex])
                    t.pendown()
                    t.left(45)
                    stackX.pop(lastIndex)
                    stackY.pop(lastIndex)
                    stackA.pop(lastIndex)
                else:
                    if (char == "["):
                        stackX.append(t.xcor())
                        stackY.append(t.ycor())
                        stackA.append(t.heading())
                        t.right(45)

def onScreenClick(x, y):
    t.penup()
    t.goto(x, y)
    drawTree(genTree("0", recursions, 0))

s = turtle.getscreen()
t = turtle.Turtle()
t.penup()

recursions = int(turtle.textinput("Recursions", "Input"))
length = int(turtle.textinput("Line Length", "Input"))
width = int(turtle.textinput("Line Width", "Input"))
speed = int(turtle.textinput("Turtle Speed", "Input"))

t.speed = speed

turtle.onscreenclick(onScreenClick)

turtle.done();
