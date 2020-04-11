def setup():
    size(600,600)
    background(50, 100, 150)
    frameRate(30)
    global slownik_kolorow, szer, wys # możńa też jednolinijkowo
    szer = 300
    wys = 0
    
    slownik_kolorow = {"rozowy":(219,112,147), "fioletowy":(218,112,214), "niebieski":(175,238,238)}
    global lista_kolorow
    lista_kolorow = []
    
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc)
    global iteracja_programu # wystarczy zadeklarować raz, nie ma potrzeby robić ego w pętli
    iteracja_programu = 560


def draw():
    global iteracja_programu
    iteracja_programu -= 1
    global szer, wys
    szer -= 1
    wys += 1
    if szer == 0:
        szer = 0
        szer += 1
    # początek dobry, szkoda, że nie dokończone
    
    stroke(255,255,255)
    strokeWeight(2)
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    rect(szer, wys, 80, 80) 

    if mousePressed:
        exit()

#1,75pkt
