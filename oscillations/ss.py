import tkinter
import os
import math

from PIL import Image, ImageTk

from vectors.vector import Vector


class Square(object):
    def __init__(self, position=None, velocity=None):
        self.img = Image.open(os.path.join('..', 'assets', 'black_square.png'))
        self.tk_img = ImageTk.PhotoImage(self.img.rotate(0))

        self.position = Vector(60, 60) if position is None else position
        self.velocity = Vector(0, 0) if velocity is None else position
        self.acceleration = Vector(0.01, 0.01)
        self.side = 17

        self.angle = 0
        self.angular_velocity = 0
        self.angular_acceleration = 0

    def update(self, canvas):
        width = int(canvas['width'])
        height = int(canvas['height'])
        if self.position.x > width:
            self.position.x = 0
        if self.position.y > height:
            self.position.y = 0

        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.angle = (math.degrees(math.atan2(self.velocity.y, self.velocity.x)))
        print(self.angle)

    def render(self, canvas):
        self.tk_img = ImageTk.PhotoImage(self.img.rotate(self.angle))
        canvas.create_image(50, 50, image=self.tk_img)

    def event_left_pressed(self, event):
        self.velocity.y += 1

    def event_right_pressed(self, event):
        self.velocity.y -= 1


class App(object):
    UPDATE_TIME = 60

    def __init__(self):
        self.objects = []

        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window,  height=200, width=200)

        self.window.bind("<Key>", self._key_pressed)
        self.window.bind("<Left>", self._left_pressed)
        self.window.bind("<Right>", self._right_pressed)
        self.canvas.bind("<Button-1>", self._mouse_1_callback)

    def _mouse_1_callback(self, event):
        print('click on:', event.x, event.y)

    def _key_pressed(self, event):
        print("Key:", event.char, event.keycode)

    def _left_pressed(self, event):
       for o in self.objects:
            o.event_left_pressed(event)

    def _right_pressed(self, event):
       for o in self.objects:
            o.event_right_pressed(event)

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
    ball = Square()
    app.add_object(ball)
    app.run()