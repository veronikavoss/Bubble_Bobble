#%%
from setting import *
#%%
class Bubble(pygame.sprite.Sprite):
    def __init__(self,asset,pos,tiles):
        super().__init__()
        self.asset=asset
        self.tiles=tiles
        self.index=0
        self.image=self.asset.bubbles['bubble_g'][self.index]
        self.rect=self.image.get_rect(center=pos)
    
    def collision(self):
        self.rect.y-=2
        for tile in self.tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.rect.top<=tile.rect.bottom:
                    self.rect.top=tile.rect.bottom
                    self.rect.x+=2
                # elif self.rect.bottom<=tile.rect.bottom and self.rect.right>=tile.rect.left:
                #     self.rect.right=tile.rect.left
                #     self.rect.x+=0
    
    def update(self):
        self.collision()

class Bubble_Launch(pygame.sprite.Sprite):
    def __init__(self,asset,pos,flip,sprite,tiles):
        super().__init__()
        self.asset=asset
        self.flip=flip
        self.bubble_sprite=sprite
        self.tiles=tiles
        
        self.index=0
        self.image=self.asset.bubbles['launch_g'][self.index]
        self.animation_speed=0.15
        self.rect=self.image.get_rect(center=pos)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=8
    
    def bubble_create(self):
        self.bubble_sprite.add(Bubble(self.asset,self.rect.center,self.tiles))
    
    def collision(self):
        for tile in self.tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.rect.right>=tile.rect.left:
                    self.kill()
                    self.bubble_create()
    
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
            self.kill()
            self.bubble_create()
        self.image=animation[int(self.index)]
    
    def update(self):
        self.collision()
        self.bubble_position()
        self.bubble_animation()