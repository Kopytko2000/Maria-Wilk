add_library('pdf')

def setup():
    global portret
    size(400, 400)
    portret = loadImage("Portret.jpg")
    beginRecord(PDF, "Portret.pdf")
    image(portret, 0, 0, height, width)
    
def draw():
    if keyPressed:
        if key == ("a"):
            image(portret, 0, 0, height, width)
            global usta
            usta = loadImage("Usta.png")
            beginRecord(PDF, "Usta.pdf")
            image(usta, 150, 264, height-300, width-350)
            endRecord()
        if key == ("d"):
            image(portret, 0, 0, height, width)
            global maska
            maska = loadImage("Maska.png")
            beginRecord(PDF, "Maska.pdf")
            image(maska, 22, 80, height-60, width-230)
            endRecord()
        if key == ("w"):
            image(portret, 0, 0, height, width)
            image(usta, 150, 264, height-300, width-350)
            image(maska, 22, 80, height-60, width-230)
        if key == ("s"):
            image(portret, 0, 0, height, width)

def mousePressed():
    exit()
