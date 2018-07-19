x=random(512)
y=random(512)
def setup():
    size(512,512)
    stroke(0)
    background(0)
    
def draw():
    global x,y
    rand=int(random(1))
    print(rand)
    
    r2=random(1)
    if r2<0.02:
        x += random(-230,230)
        y+=random(-230,230)
    
    
    
    #50% go to right
    if rand==0:
        x+=20
    #20% go to left
    if rand==1:
        x-=20
    #10% go down
    if rand==2:
        y+=20
    #20% go up
    if rand==3:
        y-=20
    rect(x-5,y-5,20,20)
    fill(100,100,255)
