#%%
from setting import *
#%%
class Assets:
    def __init__(self):
        current_path=os.path.dirname(os.path.abspath(__file__))
        image_path=os.path.join(current_path,'image')
        sound_path=os.path.join(current_path,'sound')
        
        self.sheet=pygame.image.load(os.path.join(image_path,'Bubble Bobble - General Sprites_fixed.png')).convert_alpha()
        self.tile_sheet=pygame.image.load(os.path.join(image_path,'Bubble Bobble - Level Tiles.png')).convert_alpha()
        
        self.tile_image()
        self.player_image()
        self.enemy_image()
        self.bubble_image()
    
    def tile_image(self):
        self.tile=[]
        for c in range(4):
            for r in range(25):
                t=pygame.Surface(tile_size)
                t.blit(self.tile_sheet,(0,0),(c*48+32+7,r*19+26,tile_w,tile_h))
                t=pygame.transform.scale2x(t)
                self.tile.append(t)
    
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
            'bubble_launch':self.temp[9:10],
            'run':self.temp[:5],
            'water':self.temp[6:7],
            'jump':self.temp[26:27],
            'fall':self.temp[24:25]
        }
    
    def enemy_image(self):
        self.temp=[]
        for i in range(32):
            e1=pygame.Surface(player_size)
            e1.blit(self.sheet,(0,0),(19*i+5,245,player_w,player_h))
            e1=pygame.transform.scale(e1,(player_w*4,player_h*4))
            self.temp.append(e1)
    
    def bubble_image(self):
        self.bubbles={
            'launch_g':[],
            'bubble_g':[]
        }
        for i in range(6):
            b=pygame.Surface(bubble_size)
            b.blit(self.sheet,(0,0),(5+i*18,1050,bubble_w,bubble_h))
            b=pygame.transform.scale(b,(bubble_w*4,bubble_h*4))
            self.bubbles['launch_g'].append(b)
        
        for i in range(3):
            b=pygame.Surface(bubble_size)
            b.blit(self.sheet,(0,0),(6+i*18,1072,bubble_w,bubble_h))
            b=pygame.transform.scale(b,(bubble_w*4,bubble_h*4))
            self.bubbles['bubble_g'].append(b)