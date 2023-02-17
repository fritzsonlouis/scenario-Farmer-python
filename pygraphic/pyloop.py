from graphics import *
import random

win = GraphWin("Test Graphics", 800, 800)

# Get a large number of rows and columns of circles neatly on the screen
for x in range(0, 800, 100):
    for y in range(0, 800, 100):
        circle = Circle(Point(x, y), 50)
        circle.draw(win)

# Use rectangles instead of circles
for x in range(100, 800, 200):
    for y in range(100, 800, 200):
        rectangle = Rectangle(Point(x-50, y-50), Point(x+50, y+50))
        rectangle.draw(win)

# Use lines instead of polygon
for x in range(0, 800, 100):
    line = Line(Point(0, x), Point(800, x))
    line.draw(win)

# Experiment with making custom colors
for x in range(200, 800, 200):
    for y in range(200, 800, 200):
        circle = Circle(Point(x, y), 50)
        circle.setFill("purple")
        circle.draw(win)

# Experiment with random colors
for x in range(300, 800, 200):
    for y in range(300, 800, 200):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        circle = Circle(Point(x, y), 50)
        circle.setFill(color)
        circle.draw(win)

# Pick random locations for polygons
for i in range(10):
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    triangle = Polygon(Point(x, y), Point(x+50, y+50), Point(x-50, y+50))
    triangle.draw(win)

# Make a diagonal line of shapes
for i in range(0, 800, 50):
    x = i
    y = i
    rectangle = Rectangle(Point(x, y), Point(x+50, y+50))
    rectangle.draw(win)

# Combine lines with one or more polygons
for x in range(0, 800, 100):
    line = Line(Point(0, x), Point(800, x))
    line.draw(win)
    for y in range(x, x+100, 50):
        rectangle = Rectangle(Point(y, x), Point(y+50, x+50))
        rectangle.draw(win)

# Make every other shape a different color
for x in range(0, 800, 100):
    for y in range(0, 800, 100):
        if (x+y) % 200 == 0:
            circle = Circle(Point(x, y), 50)
            circle.setFill("red")
            circle.draw(win)
        else:
            circle = Circle(Point(x, y), 50)
            circle.setFill("green")
            circle.draw(win)

# Pause the program until a mouse click
win.getMouse()
win.close()