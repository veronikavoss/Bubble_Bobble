#%%
from setting import *
from asset import *
from tile import *
from player import *
from bubble import *
#%%
class Controller:
    def __init__(self,screen):
        self.screen=screen
        
        self.level=1
        
        self.asset=Assets()
        self.tile_sprite=pygame.sprite.Group()
        self.bubble_sprite=pygame.sprite.Group()
        self.p1_sprite=pygame.sprite.GroupSingle()
        self.create_tile()
    
    def create_tile(self):
        with open('map.csv','r') as r:
            map_temp=r.readlines()
        self.map_index=[i.strip().replace(',','') for i in map_temp]
        for row,column in enumerate(self.map_index):
            for column_index,number in enumerate(column):
                x=column_index*tile_w
                y=row*tile_h+36
                if number==str(self.level):
                    self.tile=Tile(self.asset,self.level,x,y)
                    self.tile_sprite.add(self.tile)
                if number=='p':
                    self.p1=Player(self.asset,x,y,self.tile_sprite,self.bubble_sprite)
                    self.p1_sprite.add(self.p1)
    
    def update(self):
        self.p1_sprite.sprite.bubble_launch_sprite.update()
        self.p1_sprite.sprite.bubble_sprite.update()
        self.p1_sprite.update()
    
    def draw(self):
        self.screen.fill('black')
        self.tile_sprite.draw(self.screen)
        self.p1_sprite.sprite.bubble_launch_sprite.draw(self.screen)
        self.p1_sprite.sprite.bubble_sprite.draw(self.screen)
        self.p1_sprite.draw(self.screen)