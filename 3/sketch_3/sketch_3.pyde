#Bardzo przepraszam, że praca oddana po terminie. Niestety zostawianie wszystkiego na ostatnią chwilę nigdy nie wychodzi dobrze. Wystąpiły u mnie drobne problemy.
#Mimo wszystko wstawiam. Dziękuję za uwagę, serdecznie pozdrawiam.
def setup():
    size(600, 600)
    font = loadFont("BodoniMTBlack-70.vlw")
    textFont(font, 70)
    
def draw():
    clear()
    background(105, 105, 105)
    
    text("M",  width/2-70, height/2)
    text("W", width/2, height/2)
    
    k = hex(get(mouseX, mouseY)) #zapisanie koloru najechanego elementu do zmiennej k
    print(keyPressed)
    if keyPressed:
        if key == 'm' or key == 'M' or (keyCode == 37):
            fill(225, 215, 0)
            text("M",  width/2-70, height/2)
        if key == 'w' or key == 'W' or (keyCode == 39):
            fill(225, 215, 0)
            text("W",  width/2, height/2)
        
    if k != 'FF696969':
        fill(225, 215, 0)
        if mouseX < width/2:
            text("M",  width/2-70, height/2)
            # i tu też jeszcze trzebaby uwzględnić zmianę na strzałki
        else:
            text("W",  width/2, height/2)
    fill(255, 255, 255) # jeżeli robisz to w każdym przypadku, to trzeba wyciągnąć z warunku
            
    s = createShape()
    s.beginShape()
    s.fill(255,0,0,0)
    strokeWeight(15)
    s.stroke(25, 25, 112)
    s.vertex(width/2-200, height/2)
    s.vertex(width/2+90, height/2)
    s.vertex(width/2+90, height/2-200)
    s.vertex(width/2-200, height/2-200)
    s.endShape(CLOSE)
    shape(s, 55, 75)
    
    q = createShape()
    q.beginShape()
    q.fill(255,0,0,0)
    strokeWeight(5)
    q.stroke(128, 0, 0)
    q.vertex(width/2-100, height/2+50)
    q.vertex(width/2+100, height/2+50)
    q.vertex(width/2+100, height/2-100)
    q.vertex(width/2-100, height/2-100)
    q.endShape(CLOSE)
    shape(q, 0, 0)
    
    w = createShape()
    w.beginShape()
    w.fill(255,0,0,0)
    strokeWeight(15)
    w.stroke(25, 25, 112)
    w.vertex(width/2-200, height/2)
    w.vertex(width/2-160, height/2-40)
    w.vertex(width/2+90, height/2)
    w.vertex(width/2+40, height/2-40)
    w.vertex(width/2+90, height/2-200)
    w.vertex(width/2+40, height/2-160)
    w.vertex(width/2-200, height/2-200)
    w.vertex(width/2-160, height/2-160)
    w.endShape(CLOSE)
    shape(w, 55, 75)

# 1,5p
# plus do aktywności za ramkę - pierwsza klasa i wyróżnia się wśród innych prac
# uznam mimo spóźnienia, bo jest nieduże, świadome i jak dotąd jednorazowe
# posprawdzaj jak działą obecnie i przeanalizuj zmiany
