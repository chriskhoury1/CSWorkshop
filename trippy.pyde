r=0
out=False
def setup():
    size (512,512)
    global r
    background (0)
    noFill()
    stroke(255)
    r+=1
    
    
def draw():
    global r,out
    background(0)
    circles(width/2, height/2,r)
    if out:
        r-=1
    else:
        r+=1
    

def circles(x,y,s):
    ellipse (x,y,s,s)
    if s>=10:
        circles(x+s/4,y,s/3)
        circles(x-s/4,y,s/3)
        circles(x,y+s/4,s/3)
        circles(x,y-s/4,s/3)
        
def mousePressed():
    global r, out
    out= not out
