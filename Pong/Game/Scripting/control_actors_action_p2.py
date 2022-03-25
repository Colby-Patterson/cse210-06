#import constants
#from game.shared.point import Point
from game.scripting.action import Action

class ControlActorsAction(Action):

    def __init__ (self, keyboard_service):

        self._keyboard_service = keyboard_service
        #self._direction = Point(0, constants.CELL_SIZE)

    def execute(self, cast, script):

        pass

        #player 2 up
        #if self._keyboard_service.is_key_down('i'):
            #self._direction = Point(0, -constants.CELL_SIZE)

        #player 2 down
        #if self._keyboard_service.is_key_down('k'):
            #self._direction = Point(0, constants.CELL_SIZE)