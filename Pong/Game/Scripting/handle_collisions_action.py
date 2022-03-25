from game.scripting.action import Action

class HandleCollisionsAction(Action):

    def __init__(self):

        self._is_game_over = False
        self._winner = ""

    def execute(self, cast, script):

        if not self._is_game_over:
            pass
        self._handle_game_over(cast)

    def handle_collision(self, cast, script):
        ball = cast.get_first_actor("balls")
        paddle_one = cast.get_first_actor("paddle_one")
        paddle_two = cast.get_first_actor("paddle_two")
        

    def handle_game_over(self, cast):
        pass