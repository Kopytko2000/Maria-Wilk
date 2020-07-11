def setup():
    size(600,600)
    global img
    img = loadImage("Heniek.jpg") 
    background(0, 100, 0)
    font = loadFont("BodoniMTBlack-70.vlw")
    textFont(font, 40)
    strokeWeight(5)
    
def draw():
    global img
    try:
        image(img, 100, 100, 400, 400)
    except:
        fill(255, 255, 255)
        text("Brak pliku", width/2-110, height/2)
        stroke(139,0,0)
    else:
        stroke(13, 92, 169)
    finally:
        noFill()
        square(100, 100, 400)
        
#2pkt
