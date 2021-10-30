#%%
from setting import *
#%%
class Bubble(pygame.sprite.Sprite):
    def __init__(self,element):
        super().__init__()
        self.element=element
        # self.player=player
        # self.launch=launch
        
        self.index=0
        self.speed=0.15
        self.image=self.element.bubbles['launch_g'][self.index]
        self.rect=self.image.get_rect()
        
    def animation(self):
        # if self.launch:
        animation=self.element.bubbles['launch_g']
        self.index+=self.speed
        if self.index>=len(animation):
            self.index=0
        self.image=animation[int(self.index)]
        self.rect=self.image.get_rect(x=int(self.index)*32)
        self.image.set_colorkey((15,79,174))
            # self.launch=False
    
    def update(self):
        self.animation()