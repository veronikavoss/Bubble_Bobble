#%%
from setting import *
#%%
class Element:
    def __init__(self):
        current_path=os.path.dirname(os.path.abspath(__file__))
        image_path=os.path.join(current_path,'image')
        sound_path=os.path.join(current_path,'sound')
        
        self.sheet=pygame.image.load(os.path.join(image_path,'Bubble Bobble - General Sprites_fixed.png')).convert_alpha()
        self.tile_sheet=pygame.image.load(os.path.join(image_path,'Bubble Bobble - Level Tiles.png')).convert_alpha()
        
        self.player_image()
        self.tile_image()
    
    def player_image(self):
        self.temp=[]
        for i in range(2):
            for j in range(15):
                p1=pygame.Surface(player_size)
                p1.blit(self.sheet,(0,0),(21*j+6,i*20+16,player_w,player_h))
                p1=pygame.transform.scale(p1,(player_w*4,player_h*4))
                self.temp.append(p1)
        
        self.player_images={
            'standby':self.temp[:3:2],
            'run':self.temp[:5],
            'water':self.temp[6:7],
            'jump':self.temp[26:27],
            'fall':self.temp[24:25]
        }
    
    def tile_image(self):
        self.tile=[]
        for c in range(4):
            for r in range(25):
                t=pygame.Surface(player_size)
                t.blit(self.tile_sheet,(0,0),(c*48+32+7,r*19+26,player_w,player_h))
                t=pygame.transform.scale2x(t)
                self.tile.append(t)