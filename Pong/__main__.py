from game.director.director import Director
from game.director.scene_manager import SceneManager
from game.services.video_service import VideoService
from game.casting.cast import Cast
from game.scripting.script import Script

def main():
    director = Director(VideoService())
    scene_manager = SceneManager()
    cast = Cast()
    script = Script()

    director.start_game(cast, script)

