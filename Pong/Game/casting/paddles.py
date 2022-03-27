from Game.casting.actor import Actor
from constants import *
from Game.shared.point import Point
class Paddle(Actor):

    def __init__(self, body, debug = False):

        super().__init__(debug)
        self._body = body

    def get_body(self):
        
        return self._body
        
    def move_next(self):

        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_up(self):

        velocity = Point(-PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_down(self):

        velocity = Point(PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def stop_moving(self):

        velocity = Point(0, 0)
        self._body.set_velocity(velocity)