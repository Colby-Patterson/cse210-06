from game.scripting.action import Action

class MoveActorsAction(Action):

    def __init__(self):

        self._actors = []

    def execute(self, cast, script):

        self._actors - cast.get_all_actors()

        for actor in self._actors:
            actor.move_next()
