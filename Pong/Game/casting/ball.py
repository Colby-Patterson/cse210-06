import random
from Game.casting.actor import Actor


class Ball(Actor):

    def __init__(self, body, image, debug = False):

        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):

        velocity = self.body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):

        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1
        veloctiy = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):

        return self._body

    