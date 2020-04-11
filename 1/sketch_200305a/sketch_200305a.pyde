def setup():
    size(600, 600)
    point(20, 30)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    line(height, width, mouseX, mouseY)
    rect(200, 200, 200, 200)
    if mousePressed:
        rect(mouseX, mouseY, width/6, height/6) # tam gdzie się da warto używać zmiennych zależnych
    #miało się też coś zadziać, gdy nie klikamy
    
# 1,75pkt
