#%%
from setting import *
#%%
class Bubble(pygame.sprite.Sprite):
    def __init__(self,asset,player):
        super().__init__()
        self.asset=asset
        self.player=player
        
        self.index=0
        self.image=self.asset.bubbles['launch_g'][self.index]
        self.animation_speed=0.15
        self.rect=self.image.get_rect(center=(self.player.rect.centerx,self.player.rect.centery))
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=10
    
    def bubble_launch(self):
        if self.player.bubble_launched:
            self.dx=+self.speed
            self.rect.x+=self.dx
        else:
            self.kill()
        
    def bubble_animation(self):
        animation=self.asset.bubbles['launch_g']
        self.index+=self.animation_speed
        if self.index>=len(animation)-1:
            self.kill()
        self.image=animation[int(self.index)]
        self.image.set_colorkey((15,79,174))
    
    def update(self):
        self.bubble_launch()
        self.bubble_animation()
        print(self.player.bubble_launched)