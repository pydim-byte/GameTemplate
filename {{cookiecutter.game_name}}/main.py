import sys,os,pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.Clock()

    def handle_inputs(self,inputs):
        pass

    def update(self,dt):
        pass

    def draw(self):
        self.display.fill('white')
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            inputs = pygame.key.get_pressed()
            dt = self.clock.tick(FPS) / 1000
            dt = min(0.01,dt)
            self.handle_inputs(inputs)
            self.update(dt)
            self.draw()


game = Game()
game.run()
