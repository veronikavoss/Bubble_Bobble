#%%
from setting import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,element,x,y,tiles):
        super().__init__()
        self.tiles=tiles
        
        self.jumped=False
        self.collide_left=False
        self.collide_right=False
        self.collide_ceiling=False
        
        self.action='standby'
        self.index=0
        self.image=element.player_images[self.action][self.index]
        self.image.set_colorkey((15,79,174))
        self.image=pygame.transform.flip(self.image,True,False)
        self.rect=self.image.get_rect(x=x*2,y=y*2-32)
        self.dx,self.dy=0,0
        self.speed=6
        self.jump_speed=-14
        self.gravity=0.6
    
    def key_input(self):
        key_pressed=pygame.key.get_pressed()
        
        if key_pressed[pygame.K_LEFT] and not self.collide_ceiling:
            self.dx=-self.speed
        elif key_pressed[pygame.K_RIGHT] and not self.collide_ceiling:
            self.dx=self.speed
        else:
            self.dx=0
        
        if key_pressed[pygame.K_UP] and not self.jumped:
            self.dy=self.jump_speed
            self.jumped=True
        
        self.rect.x+=self.dx
    
    def collision(self):
        for tile in self.tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dx<0:
                    self.collide_left=True
                    self.rect.left=tile.rect.right
                elif self.dx>0:
                    self.collide_right=True
                    self.rect.right=tile.rect.left
        
        self.dy+=self.gravity
        self.rect.y+=self.dy
        
        for tile in self.tiles:
            if pygame.sprite.collide_mask(self,tile):
                if self.dy>=0 and self.rect.bottom>=tile.rect.top:
                    self.dy=0
                    self.rect.bottom=tile.rect.top
                    self.jumped=False
                elif self.rect.top<=tile.rect.bottom and self.dy!=0:
                    self.collide_ceiling=True
                    self.action='ceiling'
        
        if self.collide_left and self.dx>=0:
            self.collide_left=False
        elif self.collide_right and self.dx<=0:
            self.collide_right=False
        if self.collide_ceiling and self.dy>0:
            self.collide_ceiling=False
    
    def set_action(self):
        if self.dx<0:
            self.action='left'
        elif self.dx>0:
            self.action='right'
        elif self.dy<0:
            self.action='jump'
        elif self.dy>1:
            self.action='fall'
        else:
            self.action='standby'
    
    def update(self):
        self.key_input()
        self.collision()
        self.set_action()
        
        print(self.action,self.collide_left,self.collide_right,self.collide_ceiling,self.dy)