from src.controller.game_controller import GameController

def main():
    controller = GameController(size=4)
    controller.start_game()

if __name__ == "__main__":
    main()
