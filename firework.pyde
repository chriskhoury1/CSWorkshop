class Mover: 
    def __init__(self,x,y):
        self.r = 10
        self.pos=PVector(x,y)
        self.vel=PVector(0,0)
        self.acc=PVector(0,0)
        
        print('Mover object has id:' , self)
        
    def display(self):
        fill(random(255), random(255), random(255),random(255))
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
        self.acc.mult(-1)
        self.vel+=self.acc

        self.pos +=self.vel
        
            
            
def setup():
    size (600,600)
    fill(255)
    global movers
    movers = []
    
   
    
def draw():
    background(0)
    print(len(movers))
    for mover in movers:
        if mover.pos.x> width or mover.pos.x<0:
            movers.remove(mover)
        elif mover.pos.y>height or mover.pos.y<0:
            movers.remove(mover)
        mover.move_it()
        #mover.check_edges()
        mover.display()
        mover.follow()
        
        
def mousePressed():
    for  i in range (100):
        movers.append(Mover(mouseX,mouseY))
        
