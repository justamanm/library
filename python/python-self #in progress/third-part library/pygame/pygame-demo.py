import pygame


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def init(self):
        pygame.display.set_mode((self.width, self.height))
        icon =pygame.image.load("res/icon.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("你过来呀.jpg")

def main():
    window = Window(700, 800)
    window.init()

    while True:
        pygame.display.update()


if __name__ == '__main__':
    main()
