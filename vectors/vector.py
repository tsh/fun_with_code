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
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self):
        self.position.add(self.velocity)

    def update(self, canvas):
        if self.position.x <= int(canvas['height']) and self.position.y < int(canvas['width']):
            self.position.add(self.velocity)

    def render(self, canvas):
        canvas.create_circle(location.x, location.y, 7, fill='black')


class App(object):
    UPDATE_TIME = 10

    def __init__(self):
        self.objects = []

        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, bg='white', height=200, width=200)

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self):
        self.canvas.delete("all")
        for o in self.objects:
            o.update(self.canvas)
        for o in self.objects:
            o.render(self.canvas)
        self.window.after(self.UPDATE_TIME, self.render)

    def run(self):
        self.canvas.pack()
        self.render()
        self.window.mainloop()

if __name__ == '__main__':
    app = App()
    location = Vector(50, 50)
    velocity = Vector(2, 2)
    ball = Ball(location, velocity)
    app.add_object(ball)
    app.run()

