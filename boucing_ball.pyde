x=0
y=0
speedx=20
speedy=20
shoot = False

def setup():
    size(512,822)
    fill(0,0,200)
    background(0)
    
def draw():
    
    global x, y, speedx, speedy
    speedx
    speedy
    y+=speedy
    x+=speedx
    if y>= height:
        speedy*=-1
    if y<= 0:
        speedy *=-1
    if x>= width:
        speedx*=-1
    if x<= 0:
        speedx *=-1

    

    ellipse(mouseX,mouseY,40,40)
    noStroke()
    if shoot==False:
        ellipse (mouseX,mouseY,40,40)
        fill(0,255,0)
        
    else:
        ellipse (x,y,40,40)
        fill(255,0,0)
        y+=speedy
    x+=speedx
    if y>= height:
        speedy*=-1
    if y<= 0:
        speedy *=-1
    if x>= width:
        speedx*=-1
    if x<= 0:
        speedx *=-1
    
    
    
    
    print(shoot)
    
    
def mouseClicked():
    x=mouseX
    y=mouseY
    
    global shoot, x, y
    if shoot ==False:
        shoot=True
        
    else: shoot=False
    
    
