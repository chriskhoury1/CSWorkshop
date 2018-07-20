class Cube: 
    def __init__(self,x,y):
        self.pos=PVector(x,y)
        
    def gravity(self):
        self.pos.y+=2
    
    def ground(self):
        if self.pos.y==100:
            self.pos.y=100    
    def display(self):
        fill(255,0,0)
        stroke(255)
        rect(self.pos.x,self.pos.y,50,50)
        
            
            
def setup():
    size(600,600)
    global cubes
    cubes=[]
    for i in range (10):
        cubes.append(Cube(20,20))

   
def draw():
    background(0)
    rect(-1,height-100,width+5,100)
    fill(169,169,169)
    for cube in cubes:
        cube.display()
        cube.gravity()
        cube.ground()
        
    



    

    
    
    
    
