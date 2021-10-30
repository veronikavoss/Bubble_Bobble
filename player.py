#%%
from setting import *
#%%
class Player(pygame.sprite.Sprite):
    def __init__(self,element,x,y,tiles):
        super().__init__()
        self.tiles=tiles
        self.element=element
        self.jumped=False
        self.collide_left=False
        self.collide_right=False
        self.collide_ceiling=False
        self.flip=True
        self.bubble_launched=False
        self.pressed=False
        
        self.action='standby'
        self.index=0
        self.image=self.element.player_images[self.action][self.index]
        self.rect=self.image.get_rect(x=x*2,y=y*2-32)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.speed=6
        self.jump_speed=-14
        self.gravity=0.6
        
        self.animation_speed=0.1
    
    def bubble_launch(self):
        pass
    
    def key_input(self):
        key_pressed=pygame.key.get_pressed()
        
        if key_pressed[pygame.K_LEFT] and not self.collide_ceiling:
            self.flip=False
            self.dx=-self.speed
        elif key_pressed[pygame.K_RIGHT] and not self.collide_ceiling:
            self.flip=True
            self.dx=self.speed
        else:
            self.dx=0
        
        if key_pressed[pygame.K_UP] and not self.jumped and not self.action=='fall':
            self.dy=self.jump_speed
            self.jumped=True
        
        if key_pressed[pygame.K_SPACE]:
            if not self.pressed:
                self.pressed=True
        else:
            self.pressed=False
        
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
        if self.dy>6:
            self.dy=6
        
        for tile in self.tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dy>=0 and self.rect.bottom>=tile.rect.top:
                    self.dy=0
                    self.rect.bottom=tile.rect.top
                    self.jumped=False
                elif self.rect.top<=tile.rect.bottom and self.dy!=0:
                    self.collide_ceiling=True
        
        if self.collide_left and self.dx>=0:
            self.collide_left=False
        elif self.collide_right and self.dx<=0:
            self.collide_right=False
        if self.collide_ceiling and self.dy>0:
            self.collide_ceiling=False
    
    def set_action(self):
        if not self.bubble_launched:
            if self.dy<0:
                self.action='jump'
            elif self.dy>1:
                self.action='fall'
            elif self.dx!=0:
                self.action='run'
                self.animation_speed=0.1
            else:
                self.action='standby'
                self.animation_speed=0.04
        else:
            self.action='standby_launch'
            self.animation_speed=0.5
    
    def animation(self):
        animation=self.element.player_images[self.action]
        self.index+=self.animation_speed
        if self.index>=len(animation):
            self.index=0
            self.bubble_launched=False
        self.image=animation[int(self.index)]
        
        if self.flip:
            self.image=pygame.transform.flip(self.image,True,False)
        else:
            self.image=pygame.transform.flip(self.image,False,False)
        
        self.image.set_colorkey((15,79,174))
    
    def update(self):
        self.key_input()
        self.collision()
        self.set_action()
        self.animation()
        
        print(self.action,self.bubble_launched,self.pressed)