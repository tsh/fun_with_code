import tkinter


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y


# AHTUNG! monkey patching
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tkinter.Canvas.create_circle = _create_circle

if __name__ == '__main__':
    location = Vector(50, 50)
    velocity = Vector(2, 2)

    # Draw
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, bg='white', height=200, width=200)
    oval = canvas.create_circle(location.x, location.y, 7, fill='black')

    canvas.pack()
    window.mainloop()