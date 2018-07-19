numcircles=5
speeds=[0]*numcircles
params = [[0]*4] * numcircles
def setup():
    size (600,600)
    fill(255)
    noStroke()
    
        
def draw():
    global speeds, numcircles,params
    background (0)
    
    for i in range (numcircles):
        params[i][1] += 0.1 + random (-1,1)
        ellipse(i*30+15,params[i][1],15,15)
