import tkinter
from vectors.vector import Vector

class Vehicle(object):
    def __init__(self, location, velocity, target):
        self.location = location
        self.velocity = velocity
        self.acceleration = Vector(0.1, 0.1)
        self.max_speed = 1
        self.max_force = 1
        self.target = target

    def seek(self, target):
        # find vector to target
        desired = Vector.static_sub(target, self.location)
        desired.normalize()

        desired.mult(self.max_speed)

        # Reynold's formula for steering force
        steering_force = Vector.static_sub(desired, self.velocity)
        # apply force
        self.acceleration.add(steering_force)
        # recalc position
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        print(self.location.x, self.location.y)

    def update(self, canvas):
        self.seek(self.target)

    def render(self, canvas):
        # seeker
        canvas.create_circle(self.location.x, self.location.y, 7, fill='black')
        # target
        canvas.create_circle(self.target.x, self.target.y, 7, fill='red')

# AHTUNG! monkey patching
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle


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
    vh = Vehicle(location=Vector(50, 50), velocity=Vector(5, 5), target=Vector(100, 200))
    app.add_object(vh)
    app.run()

