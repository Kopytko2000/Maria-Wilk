add_library('pdf')

def setup():
    global portret, usta, maska
    size(400, 400) # to nie są proporcje zdjęcia dokumentowego
    portret = loadImage("Portret.jpg")
    usta = loadImage("Usta.png")
    maska = loadImage("Maska.png")
    beginRecord(PDF, "Portret.pdf")
    image(portret, 0, 0, height, width)
    
def draw():
    if keyPressed:
        if key == ("a"):
            image(usta, 150, 264, height-300, width-350)
        if key == ("d"):
            beginRecord(PDF, "Maska.pdf")
            image(maska, 22, 80, height-60, width-230)
        if key == ("w"):
            image(usta, 150, 264, height-300, width-350)
            image(maska, 22, 80, height-60, width-230)
        endRecord()

def mousePressed():
    exit()

#nie chodziło o to, aby każdy element z osobna zmienić z grafiki na pdf, tylko żeby w sposób zautomatyzowany umozliwić eksport zdjęć dodając na nie grafikę
#1,5pkt
