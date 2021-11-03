#%%
from setting import *
#%%
class Bubble(pygame.sprite.Sprite):
    def __init__(self,asset,pos):
        super().__init__()
        self.asset=asset
        self.index=0
        self.image=self.asset.bubbles['bubble_g'][self.index]
        self.rect=self.image.get_rect(center=pos)
    
    def update(self):
        self.rect.y+=1

class Bubble_Launch(pygame.sprite.Sprite):
    def __init__(self,asset,pos,flip):
        super().__init__()
        self.asset=asset
        self.flip=flip
        self.bubble_sprite=pygame.sprite.Group()
        
        self.index=0
        self.image=self.asset.bubbles['launch_g'][self.index]
        self.animation_speed=0.1
        self.rect=self.image.get_rect(center=pos)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=6
    
    def bubble_position(self):
        self.dx=+self.speed
        if self.flip:
            self.rect.x+=self.dx
        else:
            self.rect.x-=self.dx
    
    def bubble_animation(self):
        animation=self.asset.bubbles['launch_g']
        self.index+=self.animation_speed
        if self.index>=len(animation)-1:
            self.bubble_sprite.add(Bubble(self.asset,self.rect.center))
            self.kill()
        self.image=animation[int(self.index)]
        self.image.set_colorkey((15,79,174))
    
    def update(self):
        self.bubble_position()
        self.bubble_animation()