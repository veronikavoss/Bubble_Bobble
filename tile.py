#%%
from setting import *
#%%
class Tile(pygame.sprite.Sprite):
    def __init__(self,asset,level,x,y):
        super().__init__()
        self.image=asset.tile[level-1]
        self.image.set_colorkey((4,2,4))
        self.rect=self.image.get_rect(x=x*2,y=y*2)