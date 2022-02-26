from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

class Voxel(Button):
    def _init_(self):
        super()._init_(
            )
    
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(parent = scene,
                position = (self.position + mouse.normal),
                model = 'assets/grassblock',
                origin_y = 0.5,
                texture = 'assets/textures/grassblock_texture',
                color = color.color(0,0,random.uniform(0.9, 1)),
                
                scale = 0.5)

            if key == 'left mouse down':
                destroy(self)

class Sky(Entity):
    def _init_(self):
        super().__init__(
            
        )





            

app = Ursina()


for z in range(50):
    for x in range(50):
        y_range = [0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        y = random.choice(y_range)
        if(y == 1):
            randomval = random.random() * 10
            if randomval > 7:
                block_range = [z, z+1,z-1]
                block_place = random.choice(block_range)
                voxel = Voxel(parent = scene,
                position = (x,1,block_place),
                model = 'assets/grassblock',
                origin_y = 0.5,
                texture = 'assets/textures/grassblock_texture',
                color = color.color(0,0,random.uniform(0.9, 1)),
                
                scale = 0.5)

                voxel = Voxel(parent = scene,
                position = (x,2,z),
                model = 'assets/grassblock',
                origin_y = 0.5,
                texture = 'assets/textures/grassblock_texture',
                color = color.color(0,0,random.uniform(0.9, 1)),
                
                scale = 0.5)
            else:
                voxel = Voxel(parent = scene,
                position = (x,1,z),
                model = 'assets/grassblock',
                origin_y = 0.5,
                texture = 'assets/textures/grassblock_texture',
                color = color.color(0,0,random.uniform(0.9, 1)),
                
                scale = 0.5)


        
        else:
            voxel = Voxel(parent = scene,
                position = (x,y,z),
                model = 'assets/grassblock',
                origin_y = 0.5,
                texture = 'assets/textures/grassblock_texture',
                color = color.color(0,0,random.uniform(0.9, 1)),
                
                scale = 0.5)




        
                
player = FirstPersonController()
sky = Sky(parent = scene,
            model = 'sphere',
            texture = 'assets/textures/skybox',
            scale = 150,
            double_sided = True
)
app.run()