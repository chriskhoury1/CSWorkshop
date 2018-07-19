'''basket = [10,35,70,140,50]

def setup():
    global basket
    size(600,400)
    background(0)
    stroke(0,0,255,150)
    
    for i in range (6):
        line(0, i*height/6, width, i * height/6)
        
    noStroke()
    
    for i in range(len(basket)):
        print(basket)
        rect (i*60,height,50,-basket[i])
        '''
        
        
basket = [0,0]

def setup():
    global basket
    size(600,800)
    background(0)
    stroke(0,0,255,150)
    
    for i in range (77):
        line(0, i*height/77, width, i * height/77)
        
    noStroke()
    
   
        
def draw():
    coin=int(random(2))
    
    if coin ==0:
        basket[0] +=1
    else: basket[1] += 1
    
    for i in range(len(basket)):
        print(basket[i])
        rect (i*width/3 +width/4,height,100,-basket[i])
        
        

        

    
