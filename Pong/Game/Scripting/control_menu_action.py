from game.scripting.action import Action

class ControlMenuAction(Action):
    """stuff"""

    def __init__(self, keyboard_service, scene_manager):
        """Constructs a new ControlMenuAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._scene_manager = scene_manager

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('1'):
            self._scene_manager.prepare_scene("original_pong", cast, script)

    def _start_original_pong(self, cast, script):
        pass