from Game.casting.actor import Actor
from Game.casting.cast import Cast
from Game.casting.ball import Ball
from Game.casting.paddles import Paddles

from Game.scripting.script import Script
from Game.scripting.action import Action
from Game.scripting.control_actors_action_p1 import ControlActorsAction
from Game.scripting.control_actors_action_p2 import ControlActorsAction
from Game.scripting.draw_actors_action import DrawActorsAction
from Game.scripting.handle_collisions_action import HandleCollisionsAction
from Game.scripting.move_actors_action import MoveActorsAction
from Game.scripting.control_menu_action import ControlMenuAction
from Game.scripting.draw_menu_action import DrawMenuAction

from Game.services.keyboard_service import KeyboardService
from Game.services.video_service import VideoService

class SceneManager:

    def prepare_scene(self, scene, cast, script):
        if scene == "menu":
            self._prepare_menu_screen(cast, script)
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