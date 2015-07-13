import tkinter
import math


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def sub(self, v):
        self.x -= v.x
        self.y -= v.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            self.div(magnitude)


# AHTUNG! monkey patching
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle


class Ball(object):
    def __init__(self, position, velocity, canvas):
        self.position = position
        self.velocity = velocity
        self.canvas = canvas

    def update(self):
        self.position.add(self.velocity)

    def display(self):
        self.canvas.create_circle(location.x, location.y, 7, fill='black')

if __name__ == '__main__':
    location = Vector(50, 50)
    velocity = Vector(2, 2)

    # Draw
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, bg='white', height=200, width=200)
    oval = canvas.create_circle(location.x, location.y, 7, fill='black')

    canvas.pack()
    while True:
        canvas.move(oval, velocity.x, velocity.y)
        canvas.after(20)
        canvas.update()
    window.mainloop()