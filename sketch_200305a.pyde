def setup():
    size(600, 600)
    point(20, 30)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    line(height, width, mouseX, mouseY)
    rect(200, 200, 200, 200)
    if mousePressed:
        rect(mouseX, mouseY, 100, 100)
        
    
    
