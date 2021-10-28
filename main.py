#%%
from controller import *
#%%
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.start_screen()
    
    def start_screen(self):
        self.game_start()
    
    def game_start(self):
        self.controller=Controller(self.screen)
        self.loop()
    
    def loop(self):
        self.playing=True
        while self.playing:
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                break
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.controller.draw()

bubblebobble=Game()
pygame.quit()
#%%
