from Game.shared.point import Point


class Rectangle:
    

    def __init__(self, position, size):
        
        self._position = Point()
        self._size = Point() 

    def get_position(self):
        
        return self._position

    def get_size(self):
        
        return self._size