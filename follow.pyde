class Mover: 
    def __init__(self):
        self.r = 10
        self.pos=PVector(random(width),(random(height)))
        self.vel=PVector(0,0)
        self.acc=PVector(0,0)
        
        print('Mover object has id:' , self)
        
    def display(self):
        fill(226,88,34,255)
        stroke(255,0,0,128)
        ellipse(self.pos.x,self.pos.y,self.r,self.r)

    def move_it(self):
        self.pos.x+= random(-5,5)
        self.pos.y+= random(-5,5)
    def check_edges(self):
        if self.pos.x>width:
            self.pos.x=0
        elif self.pos.x < 0:
            self.pos.x = width
            
        if self.pos.y>height:
            self.pos.y = 0
        elif self.pos.y<0:
            self.pos.y=height
    def follow(self):
        mouse=PVector(mouseX,mouseY)
        dir = PVector.sub(mouse, self.pos)
        dir.normalize()
        
        self.acc=dir
        self.acc.mult(0.15)
        self.vel+=self.acc
        self.vel.limit(6)
        self.pos +=self.vel
        
            
            
def setup():
    size (600,600)
    fill(255)
    global movers
    movers = []
    
    for i in range (70):
        movers.append (Mover())
    
   
    
def draw():
    background(0)
    for mover in movers:
        mover.move_it()
        mover.check_edges()
        mover.display()
        mover.follow()
        
