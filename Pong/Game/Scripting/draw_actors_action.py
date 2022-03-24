from game.scripting.action import Action

class DrawActorsAction(Action):

    def __init__(self, video_service):

        self._video_service = video_service

    def execute(self, cast, script):
        
        ball = cast.get_first_actor("balls")
        paddle_one = cast.get_first_actor("paddle_one")
        paddle_two = cast.get_first_actor("paddle_two")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(paddle_one)
        self._video_service.draw_actor(paddle_two)
        self._video_service.draw_actor(ball)
        self._video_service.flush_buffer()
        