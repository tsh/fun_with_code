from vectors.vector import Vector

class Vehicle(object):
    def __init__(self):
        location = Vector()
        velocity = Vector()
        acceleration = Vector()
        max_speed = 10

    def seek(self, target):
        desired = Vector.static_sub(target, self.location)
        desired.normalize()
        desired.mult(self.max_speed)

        steering_force = Vector.static_sub(desired, self.velocity)
        self.apply_force(steering_force)

    def apply_force(self, force):
        self.acceleration.add(force)