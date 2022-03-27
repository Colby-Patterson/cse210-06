from game.scripting.script import Script
from game.casting.cast import Cast
from game.director.scene_manager import SceneManager

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._script = Script()
        self._cast = Cast()
        self.scene_manager = SceneManager()
        
    def start_game(self):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """

        self.scene_manager.prepare_scene("menu")


        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", self._cast, self._script)
            self._execute_actions("update", self._cast, self._script)
            self._execute_actions("output", self._cast, self._script)
        self._video_service.close_window()

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script)


    def change_scene(self, scene):
        self.scene_manager.prepare_scene(scene)