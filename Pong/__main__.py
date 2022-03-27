from game.director.director import Director
from game.services.video_service import VideoService

def main():
    director = Director(VideoService())
    director.start_game()

