#%%
from setting import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,element,x,y):
        super().__init__()
        player_image=element.player_images
        
        self.action='standby'
        self.image=player_image[self.action][0]
        self.image.set_colorkey((15,79,174))
        self.image=pygame.transform.flip(self.image,True,False)
        self.rect=self.image.get_rect(x=x*2,y=y*2-32)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=5
        self.jump_speed=-30
    
    def key_input(self):
        self.rect.x+=self.dx
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.dx=-self.speed
        elif key_pressed[pygame.K_RIGHT]:
            self.dx=self.speed
        else:
            self.dx=0
        if key_pressed[pygame.K_UP]:
            self.dy=self.jump_speed
    
    def collision(self):
        pass
    
    def set_action(self):
        if self.dx<0:
            self.action='left'
        elif self.dx>0:
            self.action='right'
        else:
            self.action='standby'
    
    def update(self):
        self.key_input()