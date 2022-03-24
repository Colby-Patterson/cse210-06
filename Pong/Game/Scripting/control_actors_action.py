#import constants
#from game.shard.point import Point
from game.scripting.action import Action

class ControlActorsAction(Action):

    def __init__ (self, keyboard_service):

        self._keyboard_service = keyboard_service
        #self._direction = Point(0, constants.CELL_SIZE)

    def execute(self, cast, script):

        pass