from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.ball import Ball
from game.casting.paddles import Paddles

from game.scripting.script import Script
from game.scripting.action import Action
from game.scripting.control_actors_action_p1 import ControlActorsAction
from game.scripting.control_actors_action_p2 import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.control_menu_action import ControlMenuAction
from game.scripting.draw_menu_action import DrawMenuAction

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

class SceneManager:

    def prepare_scene(self, scene, cast, script):
        if scene == "original_pong":
            self._prepare_original_pong(cast, script)

    def _prepare_menu_screen(self, cast, script):
        keyboard_service = KeyboardService()
        video_service = VideoService()

        banner = Actor()
        banner.set_text("Press 1 for original pong")
        cast.add_actor("banners", banner)

        script.add_action("input", ControlMenuAction(keyboard_service, self))
        script.add_action("update", Action())
        script.add_action("output", DrawMenuAction(video_service))


    def _prepare_original_pong(self, cast, script):
        pass