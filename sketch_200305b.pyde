def setup():
    size(600, 600)
    background(50, 100, 150)
def draw():
    if mousePressed:
        rect(mouseX, mouseY, 100, 150)
        strokeWeight(5)
        stroke(5)
        fill(20)
