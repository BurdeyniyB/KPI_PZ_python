

from graphics import *
if __name__ == "__main__":
    win = GraphWin("Вікно для графіки graphics", 600, 600)

    pol1 = Polygon(Point(100, 100), Point(75, 250), Point(125, 250), )
    pol1.setFill('red')
    pol1.setWidth(1)
    pol1.draw(win)

    pol2 = Polygon(Point(80, 220), Point(25, 125), Point(50, 250), Point(75, 250))
    pol2.setFill('blue')
    pol2.setWidth(1)
    pol2.draw(win)

    pol3 = Polygon(Point(120, 225), Point(175, 125), Point(150, 250), Point(125, 250))
    pol3.setFill('lime')
    pol3.setWidth(1)
    pol3.draw(win)

    c1 = Circle(Point(100, 100), 10)
    c1.setFill('red')
    c1.setWidth(1)
    c1.draw(win)

    c2 = Circle(Point(25, 125), 10)
    c2.setFill('blue')
    c2.setWidth(1)
    c2.draw(win)

    c3 = Circle(Point(175, 125), 10)
    c3.setFill('lime')
    c3.setWidth(1)
    c3.draw(win)

    win.getMouse()
    win.close()